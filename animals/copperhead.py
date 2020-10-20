from .animal import Animal
from movements import Slithering

class Copperhead(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Slithering.__init__(self)

  def feed(self):
    print(f'{self.name} likes to listen to classical music while eating {self.food}')