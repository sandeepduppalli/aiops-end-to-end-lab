# End-to-End AIOps Lab  
**Prometheus · ML Anomaly Detection · Correlation · Auto-Remediation Gates**

This repository contains a complete, hands-on **AIOps implementation** built using open-source tooling.  
It demonstrates how modern observability data can be used to **detect anomalies, correlate signals, perform RCA, and safely trigger automation decisions**.

This project focuses on **decision intelligence and safety-first automation**, not blind auto-fixes.

---

## 🚀 What This Project Demonstrates

- Application metrics instrumentation
- Prometheus-based monitoring
- ML-driven anomaly detection
- Correlated alerting
- Root Cause Analysis (RCA) via dashboards
- Episode timelines (incident lifecycle)
- Auto-remediation **decision gates**
- Closed-loop automation via Alertmanager webhooks (simulated)

---

## 🧠 Architecture Overview

```
Application
   ↓
Prometheus (metrics + alert rules)
   ↓
ML Anomaly Detection Exporter
   ↓
Correlated Alerts
   ↓
Auto-Remediation Decision Gates
   ↓
Alertmanager
   ↓
Automation Webhook (Safe / Simulated Action)
```

---

## 📂 Repository Structure

```
app/                # Sample application with metrics
metrics/            # Metrics / instrumentation utilities
ml/                 # ML anomaly detection exporter
automation/         # Auto-remediation webhook receiver
prometheus/         # Prometheus configs and alert rules
docker-compose.yml
README.md
```

---

## 🔑 Key AIOps Concepts Covered

- Behavioral anomaly detection (time series)
- Event correlation across metrics
- RCA using signal timelines
- Noise reduction via adaptive alerting
- Separation of decision and execution layers
- Safety-gated automation

---

## ⚠️ Disclaimer

This project **simulates auto-remediation safely**.  
No destructive or production-impacting actions are executed.

---

## 🛠 Prerequisites

- Docker & Docker Compose
- Python 3.9+
- Git

---

## ▶️ Quick Start (Recommended)

### Clone the repository

```bash
git clone https://github.com/sandeepduppalli/aiops-end-to-end-lab.git
cd aiops-end-to-end-lab
```

### Start the core stack

```bash
docker compose up
```

This starts:
- Sample application
- Prometheus
- Alertmanager

### Start supporting services

```bash
# ML anomaly exporter
python3 ml/ml_exporter.py

# Automation webhook (simulated remediation)
python3 automation/receiver.py
```

---

## 🔍 Access Points

- Application metrics: http://localhost:5000/metrics  
- Prometheus UI: http://localhost:9090  
- Alertmanager UI: http://localhost:9093  

---

## 🧪 Generate Load (Testing)

```bash
while true; do
  curl -s http://localhost:5000/ > /dev/null &
  sleep 0.05
done
```

Use Prometheus dashboards and the `/alerts` page to observe:
- Anomaly detection
- Signal correlation
- Alert lifecycle (inactive → pending → firing → resolved)
- Auto-remediation eligibility decisions

---

## 📊 Example Screenshots (What to Expect)

During testing, you should observe:

### 1. Anomaly Score Panel
- Flat baseline during normal traffic
- Sharp spike during abnormal behavior
- Gradual decay during recovery

### 2. Episode Timeline
- Traffic increases first
- Anomaly score reacts next
- Errors appear afterward
- Alerts transition through lifecycle states

### 3. RCA Summary
- Traffic-driven incidents
- Error amplification under load
- Latency impact (when applicable)

### 4. Automation Logs
- Auto-remediation approval logged only when safety gates pass
- No action logged for high-risk scenarios

---

## 👤 Author

**Sandeep Duppalli**  
Built as a hands-on AIOps learning and portfolio project.

