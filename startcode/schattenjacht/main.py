import turtle
from speler import Speler

# --- INITIALISATIE ---
scherm = turtle.Screen()
scherm.title("Draak en de Schatkisten")
scherm.bgcolor("skyblue")
scherm.setup(500, 500)
# ---------------------


gevonden_items = []
schatten = []


# Maak 3 schatten aan


def controleer_schat():
    """Kijk of speler bij een schat staat"""
    pass


# ----------------------
# Maak speler aan en geef de controleer_schat functie mee
speler = Speler(scherm, controleer_schat)

print("Gebruik de pijltjestoetsen om te bewegen!")
print("Zoek alle schatten!")

scherm.mainloop()