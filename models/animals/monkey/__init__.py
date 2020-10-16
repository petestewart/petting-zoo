from datetime import date

class Monkey:
  def __init__(self, name, species, food):
    self.name = name
    self.species = species
    self.shift = ""
    self.walking = True
    self.date_added = date.today()
    self.food = food

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def __str__(self):
    return f"{self.name} is a {self.species}"