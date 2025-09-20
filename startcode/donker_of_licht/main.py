import tkinter as tk
import requests
import datetime

def geocode(plaats):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": plaats, "count": 1, "language": "en", "format": "json"}
    resp = requests.get(url, params=params)
    data = resp.json()
    if "results" not in data or len(data["results"]) == 0:
        return None, None
    locatie = data["results"][0]
    return locatie["latitude"], locatie["longitude"]

def is_het_donker(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "daily": "sunrise,sunset", "timezone": "UTC"}
    resp = requests.get(url, params)
    data = resp.json()


    zonsopkomst = data["daily"]["sunrise"][0]
    zonsondergang = data["daily"]["sunset"][0]
    huidige_tijd = datetime.datetime.utcnow().isoformat()
    if huidige_tijd < zonsopkomst:
        return True #donker
    if huidige_tijd > zonsondergang:
        return True #donker
    return False #licht

def check_licht():
    # plaats = input('welke plaats?')
    plaats = "Hasselt"

    lat, lon = geocode(plaats)
    if lat is None:
        return
    donker = is_het_donker(lat, lon)
    if donker:
        print("Het is donker")
    else:
        print('Het is licht')

check_licht()
# --- GUI ---
root = tk.Tk()
root.title("Is het donker of licht buiten?")

tk.Label(root, text="Plaatsnaam:").grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

btn = tk.Button(root, text="Check", command=check_licht)
btn.grid(row=0, column=2, padx=5, pady=5)

label_resultaat = tk.Label(root, text="", font=("Arial", 14), justify="center")
label_resultaat.grid(row=1, column=0, columnspan=3, pady=10)

root.mainloop()
