import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocess_data(data):
    # Scale numerical features
    scaler = MinMaxScaler()
    numerical_features = ["loan_amount", "interest_rate", "term_months", "credit_score", "annual_income", "debt_to_income"]
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    # Encode categorical features
    encoder = LabelEncoder()
    data["loan_purpose"] = encoder.fit_transform(data["loan_purpose"])

    return data
