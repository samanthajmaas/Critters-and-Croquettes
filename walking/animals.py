from datetime import date

class Llama():
    def __init__(self, unique_id, name, species, shift):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

kevin = Llama("Kevin", "domesticated Llama", "morning")

class Goat():
    def __init__(self, unique_id, name, species, shift):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

gary = Goat("Gary", "billy-goat", "mid-day")

class Horse():
    def __init__(self, unique_id, name, species, shift):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

chester = Horse("Chester", "stallion", "afternoon")

class Pig():
    def __init__(self, unique_id, name, species, shift):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

oinky = Pig("Oinky", "pot-belly", "morning")

class Cow():
    def __init__(self, unique_id, name, species, shift):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True

bessy = Cow("Bessy", "milking cow", "afternoon")