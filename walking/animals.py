from datetime import date

class WalkingAnimal:
    def __init__(self, name, species, shift, food):
      self.name = name
          self.species = species
          self.shift = shift
          self.date_added = date.today()
          self.food = food

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"


class Llama():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True
    
    def feed(self)
      print(f'On {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')


class Goat():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True


class Horse():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True


class Pig():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True


class Cow():
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True
