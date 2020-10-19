from .animal import Animal

class Llama(Animal):
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.walking = True
    
    def feed(self)
      print(f'On {date.today()}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}')