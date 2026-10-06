# 🛡️ Enterprise Network Intrusion Detection System (IDS) & SOC Simulation

> **An industry-oriented defensive cybersecurity platform for network traffic monitoring, intrusion detection, anomaly analysis, security alert triage, and SOC-style incident investigation.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B)
![Machine Learning](https://img.shields.io/badge/ML-IsolationForest-orange)
![Database](https://img.shields.io/badge/Database-SQLite-003B57)
![Security](https://img.shields.io/badge/Focus-Defensive%20Cybersecurity-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

The **Enterprise Network Intrusion Detection System (IDS) & SOC Simulation** is a defensive cybersecurity project designed to simulate how a Security Operations Center (SOC) can monitor network activity, identify suspicious behavior, prioritize security alerts, and investigate potential incidents.

The platform combines:

* Synthetic network traffic generation
* Signature-based intrusion detection
* Machine-learning-based anomaly detection
* Automated risk scoring
* Security alert classification
* SOC-style incident investigation
* Interactive security dashboards
* Persistent security event logging

The project is designed for **cybersecurity education, blue-team training, secure monitoring concepts, and SOC workflow simulation**.

It does not perform unauthorized network access or real-world exploitation.

---

# 🎯 Project Objectives

The primary objectives of this project are:

1. Simulate realistic enterprise network traffic.
2. Detect known suspicious traffic patterns.
3. Identify anomalous network behavior.
4. Combine rule-based and machine-learning detection.
5. Prioritize alerts using risk scoring.
6. Simulate SOC analyst investigation workflows.
7. Maintain security audit records.
8. Visualize network security events.
9. Demonstrate defensive cybersecurity architecture.
10. Provide an industry-oriented cybersecurity portfolio project.

---

# 🚀 Key Features

## 🌐 Synthetic Network Traffic Generation

The system generates simulated network-flow data representing both legitimate and suspicious activity.

Example simulated scenarios include:

* Normal network communication
* Port scanning
* SSH brute-force attempts
* Suspicious connection bursts
* Data-exfiltration-like traffic patterns
* Abnormal network behavior

All traffic is **synthetic** and generated for defensive testing.

---

# 🔍 Dual Detection Engine

The IDS combines two complementary detection approaches.

### 1. Signature-Based Detection

Deterministic rules identify known suspicious patterns.

Examples include:

```text
Port scanning behavior
Repeated SSH connection attempts
Abnormally high connection frequency
Suspicious traffic characteristics
```

Signature-based detection is useful when the behavior matches a known rule or indicator.

---

### 2. Machine Learning Anomaly Detection

The project uses **Isolation Forest** for unsupervised anomaly detection.

The model identifies traffic that appears significantly different from the expected baseline.

This demonstrates the concept of:

```text
Normal Behavior
       ↓
Baseline Learning
       ↓
Traffic Analysis
       ↓
Anomaly Detection
       ↓
Security Alert
```

Machine learning complements, rather than replaces, deterministic security rules.

---

# ⚠️ Risk Scoring & Alert Triage

Detected events are assigned security severity levels:

| Severity    | Meaning                         |
| ----------- | ------------------------------- |
| 🟢 INFO     | Informational activity          |
| 🔵 LOW      | Low-risk event                  |
| 🟡 MEDIUM   | Potentially suspicious activity |
| 🟠 HIGH     | Significant security concern    |
| 🔴 CRITICAL | High-priority security event    |

The system generates a risk score to help prioritize alerts.

This simulates an important SOC principle:

> **Not every security event deserves the same level of response.**

---

# 🖥️ Interactive SOC Dashboard

The application provides an interactive Streamlit dashboard for security monitoring.

The dashboard can be used to:

* Monitor simulated network activity
* View security alerts
* Analyze event severity
* Investigate suspicious IP addresses
* Review detection results
* Visualize security trends
* Examine risk scores
* Generate incident reports

The interface is designed to resemble a simplified SOC monitoring environment.

---

# 📊 Security Monitoring Workflow

```text
                 ┌──────────────────────┐
                 │ Synthetic Network    │
                 │ Traffic Generator    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Network Traffic      │
                 │ Feature Extraction   │
                 └──────────┬───────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
       ┌────────────────┐      ┌──────────────────┐
       │ Signature      │      │ ML Anomaly       │
       │ Detection      │      │ Detection        │
       └───────┬────────┘      └────────┬─────────┘
               │                        │
               └───────────┬────────────┘
                           ▼
                 ┌──────────────────────┐
                 │ Detection Correlation│
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Risk Scoring &       │
                 │ Alert Classification │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ SOC Dashboard        │
                 │ Investigation        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ SQLite Security      │
                 │ Audit Log            │
                 └──────────────────────┘
```

---

# 🧠 Detection Methodology

The system follows a layered detection strategy.

### Layer 1 — Traffic Generation

Synthetic network flows are created with relevant network characteristics.

### Layer 2 — Feature Analysis

Traffic features are analyzed to identify suspicious characteristics.

### Layer 3 — Signature Detection

Known patterns are evaluated against deterministic rules.

### Layer 4 — Anomaly Detection

Isolation Forest identifies traffic that deviates from the learned/expected distribution.

### Layer 5 — Risk Assessment

Detection results are converted into security risk indicators.

### Layer 6 — SOC Investigation

Security analysts can investigate alerts through the dashboard.

---

# 🏗️ System Architecture

```text
                         ┌────────────────────┐
                         │       User         │
                         └─────────┬──────────┘
                                   │
                                   ▼
                     ┌─────────────────────────┐
                     │   Streamlit SOC UI      │
                     └────────────┬────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
          ┌──────────────────┐        ┌──────────────────┐
          │ Traffic Generator│        │ Event Database   │
          └────────┬─────────┘        │ SQLite           │
                   │                  └──────────────────┘
                   ▼
          ┌──────────────────┐
          │ Detection Engine │
          └────────┬─────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
   ┌─────────────┐    ┌──────────────┐
   │ Signatures  │    │ Isolation    │
   │ / Rules     │    │ Forest       │
   └──────┬──────┘    └──────┬───────┘
          │                  │
          └────────┬─────────┘
                   ▼
          ┌──────────────────┐
          │ Risk Scoring     │
          │ & Alert Triage   │
          └────────┬─────────┘
                   │
                   ▼
          ┌──────────────────┐
          │ SOC Investigation│
          │ & Reporting      │
          └──────────────────┘
```

---

# 📂 Project Structure

```text
network-ids-simulation/
│
├── app.py
├── generator.py
├── engine.py
├── database.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── screenshots/
│   ├── screenshot (80).png
│   ├── screenshot (81).png
│   ├── screenshot (82).png
│   ├── screenshot (83).png
│   ├── screenshot (84).png
│   └── screenshot (85).png
│
└── data/
    └── ...
```

> The exact project structure may vary depending on the implementation and generated runtime files.

---

# 🖼️ Application Screenshots

The following screenshots demonstrate the simulated SOC dashboard, network monitoring, detection results, alert triage, and security investigation functionality.

### 📊 Screenshot 1 — SOC Dashboard

![SOC Dashboard](screenshots/Screenshot%20%2880%29.png)

---

### 🔍 Screenshot 2 — Network Traffic Monitoring

![Network Monitoring](screenshots/Screenshot%20%2881%29.png)

---

### 🚨 Screenshot 3 — Security Alerts

![Security Alerts](screenshots/Screenshot%20%2882%29.png)

---

### 🧠 Screenshot 4 — Anomaly Detection

![Anomaly Detection](screenshots/Screenshot%20%2883%29.png)

---

### 📈 Screenshot 5 — Risk Analysis

![Risk Analysis](screenshots/Screenshot%20%2884%29.png)

---

### 🛡️ Screenshot 6 — SOC Investigation / Incident Report

![SOC Investigation](screenshots/Screenshot%20%2885%29.png)

> **Note:** All traffic shown in this project is synthetic and intended for educational and defensive-security simulation.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/network-ids-simulation.git
```

```bash
cd network-ids-simulation
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start the SOC Dashboard

```bash
streamlit run app.py
```

The Streamlit dashboard will then be available through the local URL displayed in the terminal.

---

# 🧰 Technologies Used

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| Python           | Core development                   |
| Streamlit        | SOC dashboard                      |
| Plotly           | Security visualization             |
| Scikit-learn     | Machine learning anomaly detection |
| Isolation Forest | Unsupervised anomaly detection     |
| SQLite           | Security event persistence         |
| Pandas           | Data processing                    |
| Git              | Version control                    |
| GitHub           | Source-code management             |

---

# 🔐 Cybersecurity Concepts Demonstrated

This project demonstrates practical knowledge of:

* Network Intrusion Detection
* Security Operations Center (SOC) Workflows
* Blue-Team Security
* Security Monitoring
* Security Alert Triage
* Threat Detection
* Signature-Based Detection
* Anomaly Detection
* Machine Learning for Cybersecurity
* Risk Scoring
* Incident Investigation
* Security Event Logging
* Defensive Security Architecture
* Security Visualization

---

# 🏢 SOC Analyst Workflow Simulation

The project demonstrates a simplified SOC workflow:

```text
1. Monitor
      ↓
2. Detect
      ↓
3. Generate Alert
      ↓
4. Assign Severity
      ↓
5. Calculate Risk
      ↓
6. Investigate
      ↓
7. Document
      ↓
8. Respond
```

This reflects the general workflow used by security monitoring and incident-response teams.

---

# 🧪 Simulated Attack Scenarios

The project uses synthetic traffic to demonstrate detection of scenarios such as:

### 🔎 Port Scan

Multiple connection attempts against different ports can indicate reconnaissance activity.

### 🔐 SSH Brute-Force Simulation

Repeated SSH connection attempts can represent suspicious authentication activity.

### 📤 Data Exfiltration Simulation

Abnormally large or unusual outbound traffic patterns can be used to demonstrate potential data-exfiltration indicators.

### 📡 Network Anomaly

Unusual traffic characteristics can be detected through the machine-learning anomaly detector.

> These scenarios are simulated locally. The project does not perform real attacks against external systems.

---

# 🤖 Machine Learning Component

The project uses **Isolation Forest**, an unsupervised anomaly-detection algorithm.

The general concept is:

```text
Training / Baseline Data
          ↓
Isolation Forest
          ↓
Learn Normal Distribution
          ↓
Analyze New Traffic
          ↓
Identify Outliers
          ↓
Generate Anomaly Alert
```

Isolation Forest is useful for demonstrating anomaly detection because it does not require a large set of manually labeled attack classes.

---

# 🗄️ Database & Security Audit Logging

SQLite is used to maintain security event information.

The database can contain information such as:

* Timestamp
* Source IP
* Destination IP
* Protocol
* Port
* Detection type
* Severity
* Risk score
* Alert description

This allows analysts to review historical security events.

---

# 📋 Alert Triage

The system prioritizes events according to severity.

Example:

```text
CRITICAL
   ↓
HIGH
   ↓
MEDIUM
   ↓
LOW
   ↓
INFO
```

This helps demonstrate how SOC analysts can focus attention on the highest-risk events first.

---

# ⚠️ Project Limitations

This is an educational SOC/IDS simulation and is **not intended to replace a production IDS, SIEM, or EDR platform**.

Important limitations include:

* Network traffic is synthetic.
* Detection rules are simplified.
* Machine-learning performance depends on the simulated dataset.
* The project does not capture live enterprise network packets by default.
* Detection results should not be treated as production-grade threat intelligence.
* Risk scores are educational indicators rather than universal security standards.
* False positives and false negatives are possible.

---

# 🔮 Future Enhancements

Potential future improvements include:

* PCAP file ingestion
* Live packet monitoring in an authorized lab
* Expanded signature/rule sets
* MITRE ATT&CK technique mapping
* SIEM integration
* Email/notification integration
* Threat-intelligence feeds
* Advanced anomaly-detection models
* Analyst case management
* Role-based access control
* Authentication for the dashboard
* Automated incident-response playbooks
* Containerized deployment
* CI/CD security testing

---

# 🧪 Recommended Testing Scenarios

The project can be tested using synthetic traffic representing:

| Scenario                        | Expected Result |
| ------------------------------- | --------------- |
| Normal traffic                  | INFO / LOW      |
| Port scanning                   | HIGH            |
| SSH brute-force                 | HIGH / CRITICAL |
| Unusual traffic volume          | MEDIUM / HIGH   |
| Data-exfiltration-like behavior | HIGH / CRITICAL |
| ML anomaly                      | Anomaly alert   |

Testing should remain within controlled, authorized environments.

---

# 🛡️ Defensive Security Principles

This project follows a defensive security philosophy:

> **Detect → Analyze → Prioritize → Investigate → Respond**

The goal is to help security teams understand suspicious network behavior and improve their ability to investigate security events.

---

# 🎓 Educational Value

This project combines multiple cybersecurity disciplines into one practical application:

```text
Networking
    +
Python Development
    +
Machine Learning
    +
Threat Detection
    +
SOC Operations
    +
Security Monitoring
    +
Incident Investigation
```

It demonstrates how different security technologies can work together to create a simplified SOC monitoring platform.

---

# 👨‍💻 Author

**Muhammed Shammas**

B.Tech Computer Science Engineering
Cybersecurity & Software Development Enthusiast

### Areas of Interest

* Cybersecurity
* SOC Operations
* Network Security
* Application Security
* Python
* Machine Learning
* Secure Coding
* Defensive Security

---

# 📜 License

This project is licensed under the **MIT License**.

---

# ⚖️ Ethical & Legal Disclaimer

This project is developed strictly for:

* Cybersecurity education
* Defensive security research
* SOC training
* Authorized security testing
* Blue-team learning
* Network-security simulation

The simulated attack scenarios are generated locally for educational purposes.

**Do not use this project to monitor, scan, attack, or investigate networks or systems without explicit authorization.**

---

# ⭐ Support

If you find this project useful for learning cybersecurity, consider giving the repository a ⭐ on GitHub.

**Built for defensive cybersecurity learning, SOC simulation, and practical security engineering.**
