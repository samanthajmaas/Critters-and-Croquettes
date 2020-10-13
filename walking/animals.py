from datetime import date

class Llama():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

kevin = Llama("Kevin", "domesticated Llama")

class Goat():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

gary = Goat("Gary", "billy-goat")

class Horse():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

chester = Horse("Chester", "stallion")

class Pig():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

oinky = Pig("Oinky", "pot-belly pig")

class Cow():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

bessy = Cow("Bessy", "milking cow")