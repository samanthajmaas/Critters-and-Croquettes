from datetime import date

class StingRay():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

ray = StingRay("Ray", "stingray")

class Goldfish():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

nemo = Goldfish("Nemo", "goldfish")

class Catfish():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

feline = Catfish("Feline", "catfish")

class Otter():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

tubs = Otter("Tubs", "otter")

class Shark():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

bruce = Shark("Bruce", "Great White Shark")