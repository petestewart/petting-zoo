from .animal import Animal
from movements import Swimming

class Eel(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    Animal.__init__(self, name, species, shift, food, chip_num)
    Swimming.__init__(self)