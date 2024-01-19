import time
from datetime import datetime
import requests

def wledClock():
    url = "****"
    current_time = datetime.now().strftime("%H:%M")
    data = {"seg": [{"id": 0, "n": current_time}]}

    try:
        response = requests.post(url, json=data)
    except requests.RequestException as e:
        print(f"Fehler beim Senden der Uhrzeit: {e}")

    now = datetime.now()
    if now.second == 0:
        current_time = datetime.now().strftime("%H:%M")
        data = {"seg": [{"id": 0, "n": current_time}]}

        try:
            response = requests.post(url, json=data)
        except requests.RequestException as e:
            print(f"Fehler beim erneuten Senden der Uhrzeit: {e}")

        time.sleep((60 - now.second) % 60)

while True:
    try:
        wledClock()
    except Exception as e:
        print(f"Fehler aufgetreten: {e}")

    time.sleep(180) 