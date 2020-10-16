class Wetlands:
  def __init__(self, name):
      self.attraction_name = name
      self.description = "beautiful aquatic wonders"
      self.animals = list()
      self.add_animal = self.animals.append

  def __str__(self):
    attraction_animals = []
    for animal in self.animals:
      # attraction_animals = attraction_animals + animal.name + ", "
      attraction_animals.append(f" * {animal.name}")
    animals_list = ('\n'.join(map(str, attraction_animals)))
    return f"{self.attraction_name} is where you'll find {self.description} like \n{animals_list}"

  @property
  def last_critter_added(self):
    return f"{self.animals[-1].name} the {self.animals[-1].species}" 