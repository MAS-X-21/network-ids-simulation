# 🛡️ Enterprise Network Intrusion Detection System (IDS) & SOC Simulation

[![Python](https://img.shields.io/badge/Python-3.10%252B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)](https://streamlit.io/)
[![Security](https://img.shields.io/badge/Cybersecurity-DEFCON-green.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An industry-oriented, end-to-end **Network Intrusion Detection System (IDS)** and **Security Operations Center (SOC)** simulation platform built in Python. This project demonstrates network traffic monitoring, signature-based rule matching, machine learning anomaly detection, automated risk scoring, and incident response investigation.

## 🚀 Key Features
- **Synthetic Network Traffic Generation**: Simulates realistic network flows including normal traffic, port scans, SSH brute-force attempts, and data exfiltration.
- **Dual Detection Engine**: Combines deterministic signature rules with Unsupervised Machine Learning (`IsolationForest`) for anomaly detection.
- **Risk Scoring & Alert Triage**: Automatically assigns severities (`INFO`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`) and risk scores to security events.
- **Interactive SOC Dashboard**: Built with Streamlit and Plotly for real-time threat visualization, IP investigation, and automated incident reporting.
- **Persistent Database**: Uses SQLite to store security audit logs.

## 📂 Project Structure
- `app.py`: Streamlit SOC Dashboard & application controller.
- `generator.py`: Synthetic network traffic generator.
- `engine.py`: Signature rules + ML anomaly detection engine.
- `database.py`: SQLite event store manager.

## ⚙️ Quick Start
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app.py`
