from flask import Flask, render_template, send_from_directory
from src import data_processing, risk_management, reporting, decision_support, utils

app = Flask(__name__)

@app.route("/")
def index():
    data = data_processing.load_data("data/sample_data.csv")
    data = data_processing.clean_data(data)
    data = data_processing.preprocess_data(data)
    data = utils.some_utility_function(data)

    risk_scores = risk_management.calculate_risk(data)
    data["calculated_risk"] = risk_scores
    risky_loans = risk_management.manage_risk(data)

    report = reporting.generate_report(data)
    visualization_path = reporting.create_visualization(data)

    decision = decision_support.make_decision(data)

    return render_template("index.html", report=report, decision=decision, visualization=visualization_path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

if __name__ == "__main__":
    app.run(debug=True)
