from animals import *
from attractions import *

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "afternoon", "barley hay", 1234)
tony = Tiger("Tony", "hungry tiger", "morning", "cat food", 234)
ned = Giraffe("Ned", "friendly giraffe", "evening", "leaves", 987)
henry = Hippo("Henry", "hippopotamus", "afternoon", "cereal", 856)
george = Monkey("George", "chimpanzee", "morning", "banana", 527)
flipper = Dolphin("Flipper", "wild dolphin", "afternoon", "plants", 2345)
buddha = Starfish("Buddha", "golden starfish", "morning", "fish food", 6723)
ed = Eel("Ed", "electric eel", "evening", "algae", 8976234)
gus = Octopus("Gus", "wild octopus", "evening", "pond scum", 9087234)
jerry = Goldfish("Jerry", "wild octopus", "morning", "fish food", 9873)
carl = Copperhead("Carl", "copperhead snake", "morning", "mice", 987234)
ren = Rat_Snake("Ren", "poisonous rattler", "afternoon", "mice", 234345)
sally = Salamander("Sally", "domestic salamander", "afternoon", "plants", 1)
charlie = Snail("Charile", "domestic snail", "afternoon", "bugs", 7)
al = Alligator("Al", "dangerous gator", "afternoon", "anything", 43)

varmint_village = PettingZoo("Varmint Village")
slither_inn = SnakePit("Slither Inn")
water_town = Wetlands("Water Town")

slither_inn.add_animal(carl)
slither_inn.add_animal(ren)
slither_inn.add_animal(sally)
slither_inn.add_animal(charlie)
slither_inn.add_animal(al)
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(tony)
varmint_village.add_animal(ned)
varmint_village.add_animal(henry)
varmint_village.add_animal(george)
water_town.add_animal(flipper)
water_town.add_animal(buddha)
water_town.add_animal(ed)
water_town.add_animal(gus)
water_town.add_animal(jerry)


print(miss_fuzz)
print(tony)
print(ned)
print(henry)
print(george)
print(flipper)
print(buddha)
print(ed)
print(gus)
print(jerry)
print(carl)
print(ren)
print(sally)
print(charlie)
print(al)
print(slither_inn)
print(varmint_village)
print(water_town)

george.chip_number = 21
print(george.chip_number)

print(slither_inn.last_critter_added)
print(varmint_village.last_critter_added)
print(water_town.last_critter_added)

al.feed()
carl.feed()
flipper.feed()