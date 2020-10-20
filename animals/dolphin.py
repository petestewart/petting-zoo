from .animal import Animal
from movements import Swimming

class Dolphin(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Swimming.__init__(self)

  def feed(self):
    print(f'{self.name} is happiest when eating {self.food}')