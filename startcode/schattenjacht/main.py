import turtle
from speler import Speler
from schat import *

# --- INITIALISATIE ---
scherm = turtle.Screen()
scherm.title("Draak en de Schatkisten")
scherm.bgcolor("skyblue")
scherm.setup(500, 500)
# ---------------------


gevonden_items = []
schatten = []


# Maak 3 schatten aan
for i in range(3):
    schatten.append(Schat())

def controleer_schat():
    for schat in schatten:
        if not schat.gevonden and schat.is_dichtbij(speler):
            gevonden_items.append(schat.item)
            print(f"Je hebt {schat.item} gevonden!")
            schat.verdwijn()

    if len(gevonden_items) == len(schatten):
        print(f"De gevonden schatten zijn:")
        for item in gevonden_items:
            print(item)
        scherm.bye()




# ----------------------
# Maak speler aan en geef de controleer_schat functie mee
speler = Speler(scherm, controleer_schat)

print("Gebruik de pijltjestoetsen om te bewegen!")
print("Zoek alle schatten!")

scherm.mainloop()