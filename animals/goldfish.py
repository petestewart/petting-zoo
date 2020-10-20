from .animal import Animal
from movements import Swimming

class Goldfish(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(name, species, food, chip_num)
    self.shift = shift
    Swimming.__init__(self)