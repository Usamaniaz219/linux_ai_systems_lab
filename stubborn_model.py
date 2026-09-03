import signal
import time
import os

def ignore_sigterm(signum, frame):
    print("SIGTERM received, but I am ignoring it!")

signal.signal(signal.SIGTERM, ignore_sigterm)

print(f"AI Model Worker Started")
print(f"PID: {os.getpid()}")

while True:
    print("Model inference worker is running...")
    time.sleep(5)
