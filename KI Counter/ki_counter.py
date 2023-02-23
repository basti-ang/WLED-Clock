import requests
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup

#scraping:

def scraping():
    global ausgabe

    URL = "https://www.kletterzentrum-innsbruck.at/"
    website = requests.get(URL)

    soup = BeautifulSoup(website.content, "html.parser")

    results = soup.find("div", class_= "bold")
    s = str(results)

    #Extrahieren von "Bouldern: 000/200"
    bouldern = re.findall(r'Bouldern:\s\d+/\d+', s)[0]

    #Extrahieren von "Seilklettern: 000/300"
    lead = re.findall(r'Seilklettern:\s\d+/\d+', s)[0]

    #Extrahieren von "Freibereich: 000/150"
    freibereich = re.findall(r'Freibereich:\s\d+/\d+', s)[0]

    # Ausgabe der Ergebnisse (debug)
    #print(bouldern)
    #print(lead)
    #print(freibereich)

    bouldernKurz = bouldern.replace("Bouldern", "B")
    leadKurz = lead.replace("Seilklettern", "L")
    freibereichKurz = freibereich.replace("Freibereich", "Out")

    ausgabe = str(bouldernKurz + " - " + leadKurz)

    # Anzeige der finalen Ausgabe (debug)
    #print(ausgabe)
    #print(len(ausgabe))



#Senden der Information an WLED:

url = "http://10.0.0.230/json/state"
scraping()
print(ausgabe) #(debug)

while True:
    if len(ausgabe) <= 32: #checkt, ob der ausgegebe String die maximale Zeichenanzahl eines Segmentnamens nicht übersteigt.
        scraping()
        data = {"seg": [{"id": 0, "n": ausgabe}]}
        response = requests.post(url, json=data)


    else:
        data = {"seg": [{"id": 0, "n": "Error"}]}
        response = requests.post(url, json=data)

    time.sleep(600) #Abfrage alle 10 Minuten