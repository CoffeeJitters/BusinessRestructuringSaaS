def some_utility_function(data):
    # Example utility function logic
    data["calculated_risk"] = data["debt_to_income"] * data["interest_rate"]
    data["risky"] = data["calculated_risk"] > 0.05
    return data
