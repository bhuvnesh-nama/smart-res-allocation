from fastapi import FastAPI
from db.mongo import reports_collection, analysis_collection
from services.pipeline import run_pipeline

app = FastAPI()


@app.get("/")
def test_db():
    try:
        data = list(reports_collection.find({}, {"_id": 0}).limit(5))
        return {
            "status": "connected",
            "sample": data
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/analyze")
def analyze():
    try:
        # STEP 1: Fetch data
        reports = list(reports_collection.find({}, {"_id": 0}))
        
        if not reports:
            return {"error": "No data found in reports collection"}

        # STEP 2: Run pipeline safely
        try:
            result = run_pipeline(reports)
        except Exception as e:
            return {
                "stage": "pipeline_error",
                "error": str(e)
            }

        # STEP 3: Store result safely
        try:
            analysis_collection.delete_many({})
            analysis_collection.insert_one(result)
        except Exception as e:
            return {
                "stage": "db_store_error",
                "error": str(e),
                "partial_result": result
            }

        return result

    except Exception as e:
        return {
            "stage": "top_level_error",
            "error": str(e)
        }