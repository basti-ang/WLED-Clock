import requests

url = "http://10.0.0.230/json/state"
data = {"seg": [{"id": 0, "n": "00:00"}]}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Segmentname wurde erfolgreich geändert")
else:
    print("Fehler beim Ändern des Segmentnamens")