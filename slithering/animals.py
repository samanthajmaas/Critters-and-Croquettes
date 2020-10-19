from datetime import date

class SlithingAnimal:
    def __init__(self, name, species, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
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



class Python():
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Crocodile():
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True



class Salamander():
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} had to be in the water to eat its {self.food}')



class Anaconda():
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True


class Gecko():
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

