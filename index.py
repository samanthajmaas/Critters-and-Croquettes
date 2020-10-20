from . attractions import PettingZoo, Wetlands, SnakePit
from animals import Goose, Python, Crocodile, Salamander, Anaconda, Gecko, StingRay, Goldfish, Catfish, Otter, Shark, Llama, Goat, Horse, Pig, Cow

silk = Python("Silk", "python", "mouse")
jaws = Crocodile("Jaws", "crocodile", "rat")
sammy = Salamander("Sammy", "salamander", "lizard food")
nicki = Anaconda("Nicki", "anaconda", "rat")
geiko = Gecko("Geiko", "gecko", "lizard food")

ray = StingRay("Ray", "stingray", "ray food")
nemo = Goldfish("Nemo", "goldfish", "fish food")
feline = Catfish("Feline", "catfish", "worms")
tubs = Otter("Tubs", "otter", "small fish")
bruce = Shark("Bruce", "Great White Shark", "small fish")

kevin = Llama("Kevin", "domesticated Llama", "morning", "llama food")
gary = Goat("Gary", "billy-goat", "mid-day", "goat food")
chester = Horse("Chester", "stallion", "afternoon", "hay")
oinky = Pig("Oinky", "pot-belly", "morning", "oats")
bessy = Cow("Bessy", "milking cow", "afternoon", "grass")
bob = Goose("Bob", "Canada goose", "watercress sandwiches")
bob.run()
bob.swim()


varmit_village = PettingZoo("Varmit Village")
crocodile_valley = SnakePit("Crocodile Valley")

crocodile_valley.add_animals(jaws)
crocodile_valley.add_animals(sammy)
crocodile_valley.add_animals(nicki)

print(crocodile_valley.last_critter_added)