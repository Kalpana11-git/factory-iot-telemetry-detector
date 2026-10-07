# Smart Factory IoT Telemetry & Anomaly Detector 🏭📊

An event-driven cloud telemetry and automated alert pipeline built on AWS to monitor industrial sensor metrics in real time and notify engineering teams during operational anomalies.

---

## 🚀 Architecture & Workflow
1. *Sensor Simulation (sensor_simulator.py):* Generates real-time IoT telemetry data (e.g., machine temperature, status) using Python.
2. *Cloud Logging & Monitoring:* Sends logs to *AWS CloudWatch* for tracking and metric evaluation.
3. *Anomaly Detection:* CloudWatch Alarms are triggered when metrics breach predefined safety thresholds (e.g., temperature > 80°C).
4. *Automated Remediation / Alerts:* Triggers an *AWS Lambda* function which securely publishes an alert message via *Amazon SNS (Simple Notification Service)* directly to the engineering team's inbox.

---

## 🛠️ Tech Stack
* *Cloud Provider:* AWS (Lambda, CloudWatch, SNS, IAM)
* *Programming Language:* Python
* *Version Control:* Git & GitHub

---

## 📂 Project Structure
```text
├── sensor_simulator.py    # Python script to simulate factory IoT sensor data
├── lambda_function.py     # AWS Lambda function for processing anomalies and triggering SNS
└── README.md              # Project documentation
