from datetime import date

class Dolphin:
  def __init__(self, name, species, food):
    self.name = ""
    self.species = ""
    self.swimming = True
    self.date_added = date.today()
    self.food = food

  def feed(self):
    print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def __str__(self):
    return f"{self.name} is a {self.species}"