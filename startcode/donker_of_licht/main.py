import tkinter as tk
import requests
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
    ...

def check_licht():
    ...
    
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
