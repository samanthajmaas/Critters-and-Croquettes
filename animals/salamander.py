from .animal import Animal

class Salamander(Animal):
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} had to be in the water to eat its {self.food}')