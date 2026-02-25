from collections import defaultdict
from parse_simple import parsing_data


def build_windows(log_file="app.log", window_size=30):
    """
    Parse logs and group events into time windows per IP.

    Returns:
        windows: list of dicts
            {
                "ip": str,
                "events": list of event dicts
            }
    """

    parsed = parsing_data(log_file)

    by_ip = defaultdict(list)

    # Group by IP
    for e in parsed:
        by_ip[e["ip"]].append(e)

    # Sort events by timestamp per IP
    for ip in by_ip:
        by_ip[ip].sort(key=lambda x: x["timestamp"])

    windows = []

    # Create time windows
    for ip, events in by_ip.items():
        window_start = events[0]["timestamp"]
        current_window = []

        for e in events:
            if e["timestamp"] - window_start <= window_size:
                current_window.append(e)
            else:
                windows.append({
                    "ip": ip,
                    "events": current_window
                })
                window_start = e["timestamp"]
                current_window = [e]

        # Add final window
        if current_window:
            windows.append({
                "ip": ip,
                "events": current_window
            })

    return windows



