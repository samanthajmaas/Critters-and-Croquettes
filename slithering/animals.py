from datetime import date

class Python():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

silk = Python("Silk", "python")

class Crocodile():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

jaws = Crocodile("Jaws", "crocodile")

class Salamander():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

sammy = Salamander("Sammy", "salamander")

class Anaconda():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

nicki = Anaconda("Nicki", "anaconda")

class Gecko():
    def __init__(self, unique_id, name, species):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

geiko = Gecko("Geiko", "gecko")