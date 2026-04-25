from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
REPORTS_COLLECTION = os.getenv("REPORTS_COLLECTION")
ANALYSIS_COLLECTION = os.getenv("ANALYSIS_COLLECTION")

if not MONGO_URI:
    raise ValueError("MONGO_URI not found in .env")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

reports_collection = db[REPORTS_COLLECTION]
analysis_collection = db[ANALYSIS_COLLECTION]