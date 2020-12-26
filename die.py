from random import randint

class Die():
    def __init__(self, num_sides=6):
        """przyjecie zalozenia ze kosci maja postac szescianu."""
        self.num_sides = num_sides

    def roll(self):
        """zwroc wartosc z zakresu od 1 do liczby scianek ktore ma kosc do gry"""
        return randint(1, self.num_sides)
