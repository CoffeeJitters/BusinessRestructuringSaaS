def calculate_risk(data):
    # Calculate risk scores based on a simple formula
    risk_scores = data["debt_to_income"] * data["interest_rate"]
    return risk_scores

def manage_risk(data):
    # Identify loans with a high risk score
    threshold = 0.05
    high_risk_loans = data[data["risk_score"] > threshold]
    return high_risk_loans
