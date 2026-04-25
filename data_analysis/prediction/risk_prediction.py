from collections import defaultdict


def predict_future_zones(reports):
    if not reports:
        return []

    pattern_map = defaultdict(int)

    for r in reports:
        location = r.get("location_name")
        issue = r.get("issue_type")

        if not location or not issue:
            continue

        pattern_map[(location, issue)] += 1

    predictions = []

    for (location, issue), count in pattern_map.items():
        if count >= 10:
            risk = "High"
        elif count >= 6:
            risk = "Medium"
        else:
            continue

        predictions.append({
            "location": location,
            "issue_type": issue,
            "predicted_risk": risk,
            "confidence": round(min(count / 15, 1.0), 2)
        })

    return predictions