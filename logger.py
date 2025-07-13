import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def write_log(script_name, message):
    date = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H:%M:%S")
    filename = f"{LOG_DIR}/{script_name}_{date}.log"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
