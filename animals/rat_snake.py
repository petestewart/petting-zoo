from .animal import Animal
from movements import Slithering

class Rat_Snake(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Slithering.__init__(self)