from .animal import Animal
from movements import Slithering

class Alligator(Animal, Slithering):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Slithering.__init__(self)

  def feed(self):
    print(f'{self.name} would prefer to eat people but will eat {self.food}')