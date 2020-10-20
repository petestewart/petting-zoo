from .attraction import Attraction
from movements import Walking

class PettingZoo(Attraction):
  def __init__(self, name):
    super().__init__(name, "cute and fuzzy critters to cuddle")

  # Duck typing check
  def add_animal_pythonic(self, animal):
    try:
      if animal.walk_speed > -1:
        self.animals.append(animal)
        print(f"{animal} now lives in {self.attraction_name}")
    except AttributeError as ex:
      print(f'{animal} doesn\'t like to be petted, so please do not put them in the {self.attraction_name} attraction.')

  # Actual typing check
  def add_animal_type_check(self, animal):
    if isinstance(animal, Walking):
      self.animals.append(animal)
      print(f"{animal} now lives in {self.attraction_name}")
    else:
      print(f'{animal} doesn\'t like to be petted, so please do not try to put them in the {self.attraction_name} attraction.')