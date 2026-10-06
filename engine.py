import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class IDSEngine:
    def __init__(self):
        self.ml_model = IsolationForest(contamination=0.15, random_state=42)
        self.is_trained = False

    def train_ml_model(self, df):
        features = df[['packet_count', 'byte_count', 'duration', 'dst_port']]
        self.ml_model.fit(features)
        self.is_trained = True

    def analyze_traffic_row(self, row):
        classification = "NORMAL"
        severity = "INFO"
        risk_score = 10
        triggered_rules = []

        if row['dst_port'] in [4444, 31337, 6667, 1337]:
            classification = "POTENTIAL INTRUSION"
            severity = "CRITICAL"
            risk_score = 95
            triggered_rules.append("Suspicious Backdoor Port Accessed")
            
        elif row['packet_count'] > 1000 and row['duration'] < 2.0:
            classification = "POTENTIAL INTRUSION"
            severity = "HIGH"
            risk_score = 85
            triggered_rules.append("Potential Port Scan / SYN Flood Detected")
            
        elif row['byte_count'] > 1000000:
            classification = "SUSPICIOUS"
            severity = "MEDIUM"
            risk_score = 65
            triggered_rules.append("High Volume Data Transfer (Potential Exfiltration)")
            
        elif row['packet_count'] > 200 and row['dst_port'] == 22:
            classification = "SUSPICIOUS"
            severity = "MEDIUM"
            risk_score = 60
            triggered_rules.append("Potential SSH Brute Force Attempt")

        if self.is_trained and classification == "NORMAL":
            features = pd.DataFrame([[row['packet_count'], row['byte_count'], row['duration'], row['dst_port']]],
                                      columns=['packet_count', 'byte_count', 'duration', 'dst_port'])
            prediction = self.ml_model.predict(features)[0]
            if prediction == -1:
                classification = "SUSPICIOUS"
                severity = "LOW"
                risk_score = 45
                triggered_rules.append("Statistical Anomaly (Unusual Flow Profile)")

        return {
            'classification': classification,
            'severity': severity,
            'risk_score': risk_score,
            'triggered_rules': ", ".join(triggered_rules) if triggered_rules else "None"
        }

    def process_dataset(self, df):
        self.train_ml_model(df)
        results = []
        for _, row in df.iterrows():
            res = self.analyze_traffic_row(row)
            res_combined = {**row.to_dict(), **res}
            results.append(res_combined)
        return pd.DataFrame(results)
