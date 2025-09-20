import turtle
import random


MOGELIJKE_ITEMS = ["diamant", "gouden munt", "zilverstaaf", "robijn", "toverring", "kaas"]

class Schat:
    def __init__(self):
        self.item = random.choice(MOGELIJKE_ITEMS)
        self.x = random.randint(-200, 200)
        self.y = random.randint(-200, 200)
        self.gevonden = False

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