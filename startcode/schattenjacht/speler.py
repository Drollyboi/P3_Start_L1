import turtle


class Speler:
    def __init__(self, scherm, na_beweging_functie):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color("green")
        self.turtle.penup()
        self.turtle.speed(0)

        self.scherm = scherm
        self.na_beweging = na_beweging_functie
        self._setup_toetsen()

    def positie(self):
        """Geef de huidige positie van de speler"""
        return self.turtle.position()

    def beweeg(self, richting):
        """Beweeg de speler in de gegeven richting"""
        if richting == "links":
            self.turtle.setheading(180)
        elif richting == "rechts":
            self.turtle.setheading(0)
        elif richting == "omhoog":
            self.turtle.setheading(90)
        elif richting == "omlaag":
            self.turtle.setheading(270)

        self.turtle.forward(20)
        self.na_beweging()  # Roep de functie aan na elke beweging

    def _setup_toetsen(self):
        """Koppel toetsen aan bewegingen"""
        self.scherm.listen()
        self.scherm.onkey(lambda: self.beweeg("links"), "Left")
        self.scherm.onkey(lambda: self.beweeg("rechts"), "Right")
        self.scherm.onkey(lambda: self.beweeg("omhoog"), "Up")
        self.scherm.onkey(lambda: self.beweeg("omlaag"), "Down")