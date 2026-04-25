from data_analysis.analysis.risk_analysis import analyze_high_risk_zones
from data_analysis.prediction.risk_prediction import predict_future_zones


def run_pipeline(reports):
    high_risk = analyze_high_risk_zones(reports)
    predicted = predict_future_zones(reports)

    return {
        "high_risk_zones": high_risk,
        "predicted_zones": predicted
    }