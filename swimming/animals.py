from datetime import date

class SwimmingAnimal:
    def __init__(self, name, species, food):
      self.name = name
          self.species = species
          self.shift = shift
          self.date_added = date.today()
          self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class StingRay():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True


class Goldfish():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True

class Catfish():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True


class Otter():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True


class Shark():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True
