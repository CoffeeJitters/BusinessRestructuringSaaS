def make_decision(data):
    # Example decision-making logic
    if len(data[data['risky']]) / len(data) > 0.1:
        decision = "The proportion of risky loans is too high. Consider tightening lending criteria."
    else:
        decision = "The proportion of risky loans is acceptable."
    return decision
