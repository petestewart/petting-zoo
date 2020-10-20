class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
      attraction_animals = []
      for animal in self.animals:
        attraction_animals.append(f" * {animal.name}")
      animals_list = ('\n'.join(map(str, attraction_animals)))
      return f"{self.attraction_name} is where you'll find {self.description} like \n{animals_list}"

    def __len__(self):
        return len(self.animals)

    @property
    def last_critter_added(self):
      return f"{self.animals[-1].name} the {self.animals[-1].species}" 