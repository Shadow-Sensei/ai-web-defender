from windowing import build_windows

feature_rows = []

WINDOW_SIZE = 30
windows = build_windows('app.log',window_size=WINDOW_SIZE)
for w in windows:
    events = w["events"]
    times = [e["timestamp"] for e in events]
    times.sort()

    deltas = [
        times[i+1] - times[i]
        for i in range(len(times) - 1)
    ]

    feature_rows.append({
        "requests": len(events),
        "fails": sum(1 for e in events if e["event"] == "LOGIN_FAIL"),
        "avg_delta": sum(deltas)/len(deltas) if deltas else WINDOW_SIZE
    })

print(feature_rows)
