from datetime import date

class Llama():
    def __init__(self, unique_id, name, species, shift, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

kevin = Llama("Kevin", "domesticated Llama", "morning", "llama food")

class Goat():
    def __init__(self, unique_id, name, species, shift, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

gary = Goat("Gary", "billy-goat", "mid-day", "goat food")

class Horse():
    def __init__(self, unique_id, name, species, shift, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

chester = Horse("Chester", "stallion", "afternoon", "hay")

class Pig():
    def __init__(self, unique_id, name, species, shift, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

oinky = Pig("Oinky", "pot-belly", "morning", "oats")

class Cow():
    def __init__(self, unique_id, name, species, shift, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

bessy = Cow("Bessy", "milking cow", "afternoon", "grass")