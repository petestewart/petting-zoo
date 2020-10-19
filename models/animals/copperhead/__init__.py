from animals import Animal

class Copperhead(Animal):

  def __init__(self, name, species, shift, food, chip_num):
    super().__init__(name, species, food, chip_num)
    self.shift = shift
    self.slithering = True

  def feed(self):
    print(f'{self.name} likes to listen to classical music while eating {self.food}')