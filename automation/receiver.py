from flask import Flask, request
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/remediate", methods=["POST"])
def remediate():
    payload = request.json
    now = datetime.utcnow().isoformat()

    alert = payload["alerts"][0]
    alert_name = alert["labels"].get("alertname")
    severity = alert["labels"].get("severity")

    if severity == "automation":
        msg = f"[{now}] AUTO-REMEDIATION APPROVED: {alert_name}"
    else:
        msg = f"[{now}] ALERT RECEIVED (NO ACTION): {alert_name}"

    print(msg)
    print(json.dumps(payload, indent=2))

    return "", 200

if __name__ == "__main__":
    print("Automation receiver running on port 7000")
    app.run(host="0.0.0.0", port=7000)

