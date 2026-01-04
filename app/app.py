from flask import Flask
import time
import random

from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# ---- Metrics ----
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    ["endpoint"]
)

ERROR_COUNT = Counter(
    "http_request_errors_total",
    "Total HTTP request errors",
    ["endpoint"]
)

# ---- Routes ----
@app.route("/")
def index():
    start = time.time()

    # Simulate some work
    time.sleep(random.uniform(0.05, 0.2))


    if random.random() < 0.03:  # ~3% errors
        ERROR_COUNT.labels(endpoint="/").inc()
        REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
        REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start)
        return "Error\n", 500

    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start)

    return "OK\n"


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

