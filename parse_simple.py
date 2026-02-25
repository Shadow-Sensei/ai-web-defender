from datetime import datetime

ALLOWED_EVENTS = {
    "LOGIN_ATTEMPT",
    "LOGIN_FAIL",
    "LOGIN_SUCCESS"
}

def parsing_data(log_file="app.log"):
    parsed = []

    with open(log_file) as f:
        for line in f:
            if "EVENT=" not in line:
                continue

            parts = line.split("|")

            event = parts[2].strip().split("=")[1]

            if event not in ALLOWED_EVENTS:
                continue

            timestamp_str = parts[0].strip()
            ip = parts[3].strip().split("=")[1]

            ts = datetime.strptime(
                timestamp_str,
                "%Y-%m-%d %H:%M:%S,%f"
            ).timestamp()

            parsed.append({
                "timestamp": ts,
                "event": event,
                "ip": ip
            })

    return parsed
