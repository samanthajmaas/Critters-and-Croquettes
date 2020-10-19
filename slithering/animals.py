from datetime import date

class Python():
    def __init__(self, unique_id, name, species, food, chip_num):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food
        self.__chip_number = chip_num
    
    @property
    def chip_num(self):
        return self.__chip_number

    @chip_num.setter 
        def chip_num(self, number):
            pass

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Crocodile():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Salamander():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Anaconda():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"



class Gecko():
    def __init__(self, unique_id, name, species, food):
        self.id = unique_id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

