# security.py
from ml_model import predict_risk
import time
from flask import request, abort

REQUESTS = {}

WINDOW = 30          # seconds
MAX_REQUESTS = 10    # allowed per window
COOLDOWN = 60        # seconds


def get_client_ip():
    """
    Get real client IP (proxy-safe).
    """
    return request.headers.get("X-Forwarded-For", request.remote_addr)


def extract_features(data, now):
    requests = data["count"]
    fails = data.get("fails", 0)

    avg_delta = max(
        (now - data["window_start"]) / max(requests, 1),
        0.01
    )

    return [requests, fails, avg_delta]

def init_soft_rate_limit(app):

    @app.before_request
    def soft_rate_limit():
        ip = get_client_ip()
        now = time.time()

        data = REQUESTS.get(ip)

        # --- Cooldown check FIRST ---
        if data and now < data["cooldown_until"]:
            app.logger.warning(
                f"EVENT=COOLDOWN_ACTIVE | IP={ip}"
            )
            abort(429)

        # --- First request from IP ---
        if not data:
            REQUESTS[ip] = {
                "count": 1,
                "window_start": now,
                "cooldown_until": 0
            }
            return

        # --- Reset window ---
        if now - data["window_start"] > WINDOW:
            data["count"] = 1
            data["window_start"] = now
            return

        # --- Increment request count ---
        data["count"] += 1
        features = extract_features(data, now)
        risk = predict_risk(features)

        app.logger.info(
        f"EVENT=RISK_EVALUATED | IP={ip} | RISK={round(risk, 3)}"
)

        if risk > 0.09:
            data["cooldown_until"] = now + COOLDOWN
            app.logger.critical(
            f"EVENT=ML_COOLDOWN | IP={ip}"
    )
            abort(429)

        elif risk > 0.024:
            delay = 3
            app.logger.warning(
            f"EVENT=ML_SLOWDOWN | IP={ip} | DELAY={delay}s"
        )
            time.sleep(delay)
        # --- Progressive slowdown ---
        if data["count"] > MAX_REQUESTS:
            delay = min(data["count"] - MAX_REQUESTS, 5)
            app.logger.warning(
                f"EVENT=SLOWDOWN | IP={ip} | DELAY={delay}s | COUNT={data['count']}"
            )
            time.sleep(delay)

        # --- Enter cooldown ---
        if data["count"] > MAX_REQUESTS + 5:
            data["cooldown_until"] = now + COOLDOWN
            app.logger.critical(
                f"EVENT=COOLDOWN_STARTED | IP={ip} | DURATION={COOLDOWN}s"
            )
