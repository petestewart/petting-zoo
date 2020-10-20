from .animal import Animal
from movements import Walking

class Hippo(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Walking.__init__(self)