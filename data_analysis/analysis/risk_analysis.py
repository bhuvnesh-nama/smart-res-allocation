import numpy as np
from sklearn.cluster import DBSCAN
from datetime import datetime


def severity_weight(severity):
    return {"High": 3, "Medium": 2, "Low": 1}.get(str(severity), 1)


def recency_weight(date_str):
    try:
        report_date = datetime.fromisoformat(str(date_str))
        days_old = (datetime.now() - report_date).days

        if days_old <= 3:
            return 1.5
        elif days_old <= 7:
            return 1.2
        else:
            return 1.0
    except Exception:
        return 1.0


def cluster_reports(reports):
    if not reports or len(reports) < 3:
        return [-1] * len(reports)

    coords = []
    valid_indices = []

    # Extract valid lat/lng safely
    for i, r in enumerate(reports):
        lat = r.get("lat")
        lng = r.get("lng")

        try:
            if lat is None or lng is None:
                continue

            lat = float(lat)
            lng = float(lng)

            coords.append([lat, lng])
            valid_indices.append(i)

        except (ValueError, TypeError):
            continue

    # Not enough valid points
    if len(coords) < 3:
        return [-1] * len(reports)

    coords = np.array(coords)
    coords = np.radians(coords)

    kms_per_radian = 6371.0088
    epsilon = 25 / kms_per_radian  # 25 km radius

    try:
        db = DBSCAN(eps=epsilon, min_samples=3, metric="haversine")
        cluster_labels = db.fit_predict(coords)
    except Exception:
        return [-1] * len(reports)

    # Map clusters back to original reports
    full_clusters = [-1] * len(reports)

    for idx, label in zip(valid_indices, cluster_labels):
        full_clusters[idx] = int(label)

    return full_clusters


def analyze_high_risk_zones(reports):
    if not reports:
        return []

    clusters = cluster_reports(reports)
    cluster_data = {}

    for i, cluster_id in enumerate(clusters):
        if cluster_id == -1 or i >= len(reports):
            continue

        r = reports[i]

        lat = r.get("lat")
        lng = r.get("lng")

        if lat is None or lng is None:
            continue

        if cluster_id not in cluster_data:
            cluster_data[cluster_id] = {
                "points": [],
                "score": 0,
                "count": 0,
                "issue_counts": {}
            }

        score = severity_weight(r.get("severity")) * recency_weight(r.get("date"))

        cluster_data[cluster_id]["points"].append((lat, lng))
        cluster_data[cluster_id]["score"] += score
        cluster_data[cluster_id]["count"] += 1

        issue = r.get("issue_type", "Unknown")
        cluster_data[cluster_id]["issue_counts"][issue] = \
            cluster_data[cluster_id]["issue_counts"].get(issue, 0) + 1

    zones = []

    for data in cluster_data.values():
        if data["count"] == 0:
            continue

        lats = [p[0] for p in data["points"]]
        lngs = [p[1] for p in data["points"]]

        center_lat = sum(lats) / len(lats)
        center_lng = sum(lngs) / len(lngs)

        avg_score = data["score"] / data["count"]

        if avg_score >= 3:
            risk_level = "High"
        elif avg_score >= 2:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        dominant_issue = max(data["issue_counts"], key=data["issue_counts"].get)

        zones.append({
            "center": [center_lat, center_lng],
            "radius_km": 25,
            "risk_level": risk_level,
            "incident_count": data["count"],
            "avg_score": round(avg_score, 2),
            "issue_type": dominant_issue
        })

    return zones