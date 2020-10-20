from .animal import Animal
from movements import Walking

class Giraffe(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(name, species, food, chip_num)
    self.shift = shift
    Walking.__init__(self)