class RGBKleur:
    def __init__(self, rood, groen, blauw):
        self.rood = rood
        self.groen = groen
        self.blauw = blauw

    def afstand_tot(self, andere):
        verschil_r = (self.rood - andere.rood) ** 2
        verschil_g = (self.groen - andere.groen) ** 2
        verschil_b = (self.blauw - andere.blauw) ** 2
        return int((verschil_r + verschil_g + verschil_b) ** 0.5)


def lees_rgb_input(speler):
    invoer = input(f"{speler}, geef jouw gok (R G B): ")
    delen = invoer.strip().split()
    if len(delen) != 3 or not all(d.isdigit() for d in delen):
        print("⚠️ Geef drie gehele getallen gescheiden door spaties.")
    return RGBKleur(int(delen[0]), int(delen[1]), int(delen[2]))