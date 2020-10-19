class Wetlands:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Have you always wanted to swim with the sharks? Well, here is your chance"
        self.animals = list()

    def add_animals(self, animal):
      return self.animals.append(animal)

    @property
    def last_critter_added():
        return self.animals.reverse()

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Snakes of all kinds but also some fun other slithering creatures"
        self.animals = list()

    def add_animals(self, animal):
      return self.animals.append(animal)

    @property
    def last_critter_added():
        return self.animals.reverse()

class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "All of the cute and fuzzy critters to cuddle!"
        self.animals = list()

    def add_animals(self, animal):
      return self.animals.append(animal)

    @property
    def last_critter_added():
        return self.animals.reverse()
