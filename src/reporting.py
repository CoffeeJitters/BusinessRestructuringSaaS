import matplotlib.pyplot as plt

def generate_report(data):
    # Example report generation logic
    report = f"Total loans: {len(data)}\nRisky loans: {len(data[data['risky']])}"
    return report

def create_visualization(data):
    # Example visualization creation logic
    plt.scatter(data["debt_to_income"], data["interest_rate"], c=data["risky"], alpha=0.5)
    plt.xlabel("Debt-to-Income Ratio")
    plt.ylabel("Interest Rate")
    plt.title("Loan Risk Visualization")
    plt.savefig("risk_visualization.png")
    return "risk_visualization.png"
