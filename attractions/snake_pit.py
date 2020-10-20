from .attraction import Attraction
from movements import Slithering

class SnakePit(Attraction):
  def __init__(self, name):
    super().__init__(name, "stupendous snakes of all sizes")

  def add_animal_pythonic(self, animal):
    try:
      if animal.slither_speed > -1:
        self.animals.append(animal)
        print(f"{animal} now lives in {self.attraction_name}")
    except AttributeError as ex:
      print(f'{animal} doesn\'t slither, so please do not put them in the {self.attraction_name} attraction.')

  # Actual typing check
  def add_animal_type_check(self, animal):
    if isinstance(animal, Slithering):
      self.animals.append(animal)
      print(f"{animal} now lives in {self.attraction_name}")
    else:
      print(f'{animal} doesn\'t slither, so please do not try to put them in the {self.attraction_name} attraction.')