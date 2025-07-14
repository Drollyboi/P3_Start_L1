import turtle


MOGELIJKE_ITEMS = ["diamant", "gouden munt", "zilverstaaf", "robijn", "toverring"]

class Schat:
    def __init__(self):
        self.item = None
        self.x = None
        self.y = None
        self.gevonden = None

        # Maak de schat zichtbaar op de juiste plaats
        self.tekenaar = turtle.Turtle()
        self.tekenaar.shape("square")
        self.tekenaar.color("gold")
        self.tekenaar.penup()
        self.tekenaar.speed(0)
        self.tekenaar.goto(self.x, self.y)

    def verdwijn(self):
        """Verberg de schat als hij gevonden is"""
        self.gevonden = True
        self.tekenaar.hideturtle()

    def is_dichtbij(self, speler):
        """Controleer of de speler dicht genoeg bij de schat is"""
        speler_x, speler_y = speler.positie()
        return abs(speler_x - self.x) < 20 and abs(speler_y - self.y) < 20