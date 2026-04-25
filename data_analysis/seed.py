import random
from datetime import datetime, timedelta
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Mongo connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
reports_collection = db[os.getenv("REPORTS_COLLECTION")]

# Clear old data (optional for fresh runs)
reports_collection.delete_many({})

# Base locations (you can tweak)
locations = [
    {"name": "Delhi", "lat": 28.6139, "lng": 77.2090},
    {"name": "Jaipur", "lat": 26.9124, "lng": 75.7873},
    {"name": "Kolkata", "lat": 22.5726, "lng": 88.3639},
    {"name": "Chennai", "lat": 13.0827, "lng": 80.2707},
    {"name": "Mumbai", "lat": 19.0760, "lng": 72.8777},
    {"name": "Bengaluru", "lat": 12.9716, "lng": 77.5946},
    {"name": "Hyderabad", "lat": 17.3850, "lng": 78.4867},
    {"name": "Patna", "lat": 25.5941, "lng": 85.1376},
]

issue_types = ["Water Shortage", "Health", "Food"]
severities = ["High", "Medium", "Low"]

def random_date():
    return datetime.now() - timedelta(days=random.randint(0, 15))

data = []

for i in range(100):
    loc = random.choice(locations)

    # Add slight geo-noise for clustering feel
    lat = loc["lat"] + random.uniform(-0.02, 0.02)
    lng = loc["lng"] + random.uniform(-0.02, 0.02)

    # Create patterns (important!)
    if loc["name"] == "Ranchi":
        issue = "Water Shortage"
        severity = random.choices(["High", "Medium"], weights=[0.7, 0.3])[0]
    elif loc["name"] == "Area_B":
        issue = "Health"
        severity = random.choice(severities)
    else:
        issue = random.choice(issue_types)
        severity = random.choice(severities)

    data.append({
        "report_id": f"r{i}",
        "lat": round(lat, 6),
        "lng": round(lng, 6),
        "location_name": loc["name"],
        "issue_type": issue,
        "severity": severity,
        "date": random_date().isoformat()
    })

# Insert
reports_collection.insert_many(data)

print("100 dummy records inserted successfully!")