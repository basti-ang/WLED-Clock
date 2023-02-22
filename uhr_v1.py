import requests
import time
from datetime import datetime

url = "http://10.0.0.230/json/state"

while True:
    now = datetime.now()
    if now.second == 0:
        current_time = datetime.now().strftime("%H:%M")
        data = {"seg": [{"id": 0, "n": current_time}]}
        response = requests.post(url, json=data)

    time.sleep((60 - now.second) % 60)

