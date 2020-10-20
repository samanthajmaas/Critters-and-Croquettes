from .animal import Animal
from movements import Walking, Swimming

class Goose(Animal, Walking, Swimming):

    def __init__(self, name, species, food):
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True
        ...
    
    def honk(self): 
        print("The goose honks. A lot")

    def __str__(self):
        return f'{self.name} the Goose'