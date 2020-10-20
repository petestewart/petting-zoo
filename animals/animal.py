from datetime import date

class Animal:
  def __init__(self, name, species, shift, food, chip_num):
    self.name = name
    self.species = species
    self.shift = shift
    self.food = food
    self.__chip_number = chip_num
    self.date_added = date.today()
    # self.walk_speed = -1

  def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  def __str__(self):
        return f'{self.name} the {self.species}'
      
  @property
  def chip_number(self):
    return self.__chip_number

  @chip_number.setter
  def chip_number(self, num):
    pass
  