import time
import requests
import pandas as pd
from sklearn.ensemble import IsolationForest

from prometheus_client import Gauge, start_http_server

PROM_URL = "http://172.31.12.194:9090"
QUERY = "rate(http_requests_total[5m])"

ANOMALY_SCORE = Gauge(
    "aiops_anomaly_score",
    "AIOps anomaly confidence score",
    ["metric"]
)


def fetch_timeseries(minutes=10):
    end = int(time.time())
    start = end - (minutes * 60)

    response = requests.get(
        f"{PROM_URL}/api/v1/query_range",
        params={
            "query": QUERY,
            "start": start,
            "end": end,
            "step": 15
        }
    )

    data = response.json()["data"]["result"]
    if not data:
        return None

    values = data[0]["values"]
    df = pd.DataFrame(values, columns=["timestamp", "value"])
    df["value"] = df["value"].astype(float)

    return df


def compute_anomaly_score(df):
    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(df[["value"]])

    raw_score = -model.decision_function(df[["value"]].tail(1))[0]

    # Normalize to 0–1
    score = min(max(raw_score * 10, 0.0), 1.0)
    return score


if __name__ == "__main__":
    start_http_server(8000)
    print("AIOps ML exporter running on port 8000")

    while True:
        df = fetch_timeseries()


        if df is None:
            print("DEBUG: No data returned from Prometheus")
        elif len(df) <= 10:
            print(f"DEBUG: Not enough data points yet: {len(df)}")
        else:
            score = compute_anomaly_score(df)
            ANOMALY_SCORE.labels(metric="http_requests_rate").set(score)
            print(f"Updated anomaly score: {score:.2f}")
        time.sleep(30)

