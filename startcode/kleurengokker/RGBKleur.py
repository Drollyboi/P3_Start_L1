class RGBKleur:
    def __init__(self, rood, groen, blauw):
        self.rood = rood
        self.groen = groen
        self.blauw = blauw



def lees_rgb_input(speler):
    invoer = input(f"{speler}, geef jouw gok (R G B): ")
    delen = invoer.strip().split()
    if len(delen) != 3 or not all(d.isdigit() for d in delen):
        print("⚠️ Geef drie gehele getallen gescheiden door spat    ies.")
    return RGBKleur(int(delen[0]), int(delen[1]), int(delen[2]))