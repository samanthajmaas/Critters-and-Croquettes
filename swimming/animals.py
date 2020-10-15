from datetime import date

class StingRay():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

ray = StingRay("Ray", "stingray", "ray food")

class Goldfish():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

nemo = Goldfish("Nemo", "goldfish", "fish food")

class Catfish():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

feline = Catfish("Feline", "catfish", "worms")

class Otter():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

tubs = Otter("Tubs", "otter", "small fish")

class Shark():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

bruce = Shark("Bruce", "Great White Shark", "small fish")