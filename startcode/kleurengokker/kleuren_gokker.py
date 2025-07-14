import turtle
import random
from RGBKleur import *

# Turtle setup
scherm = turtle.Screen()
scherm.colormode(255)

# Spelsetup
score_speler1 = 0
score_speler2 = 0
aantal_rondes = 3

print("🎮 Welkom bij Kleurengokker!\n")

for ronde in range(aantal_rondes):
    print(f"\n🔁 Ronde {ronde + 1}")

    random_rood = random.randint(0, 255)
    random_groen = random.randint(0, 255)
    random_blauw = random.randint(0, 255)
    geheime_kleur = RGBKleur(random_rood, random_groen, random_blauw)
    scherm.bgcolor(random_rood, random_groen, random_blauw)
    print("🎨 Kijk naar het kleur en raad de RGB-waarde.")

    gok1 = lees_rgb_input("Speler 1")
    gok2 = lees_rgb_input("Speler 2")

    print(f"🔎 De echte kleur was RGB({random_rood}, {random_groen}, {random_blauw})")

    afstand1 = gok1.afstand_tot(geheime_kleur)
    afstand2 = gok2.afstand_tot(geheime_kleur)

    print(f"📏 Speler 1 zat er {afstand1} naast.")
    print(f"📏 Speler 2 zat er {afstand2} naast.")

    if afstand1 < afstand2:
        print("✅ Speler 1 wint deze ronde!")
    elif afstand2 < afstand1:
        print("✅ Speler 2 wint deze ronde!")
    else:
        print("⚖️ Gelijkspel!")

    score_speler1 += afstand1
    score_speler2 += afstand2

    if ronde != 2:
        input("⏎ Druk op ENTER om naar de volgende ronde te gaan...")

# Einde
print("\n🏁 Einde spel!")
print(f"Speler 1 totaalafstand: {score_speler1}")
print(f"Speler 2 totaalafstand: {score_speler2}")
if score_speler1 < score_speler2:
    print("🥇 Speler 1 wint!")
elif score_speler2 < score_speler1:
    print("🥇 Speler 2 wint!")
else:
    print("🤝 Gelijkspel!")

# Sluit het turtle-venster
scherm.bye()