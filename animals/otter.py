from .animal import Animal

class Otter(Animal):
    def __init__(self, name, species, shift, food):
        super().__init__(name, species, shift, food)
        self.swimming = True
