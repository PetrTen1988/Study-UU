class Animal:
    def __init__(self, name, alive, fed):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    edible: bool

    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name, alive = True, fed = False):
        super().__init__(name, alive, fed)

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Mammal(Animal):
    def __init__(self, name, alive = True, fed = False):
        super().__init__(name,alive, fed)

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    def __init__(self, name):
        self.edible = False
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        self.edible = True
        super().__init__(name)




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
#
print(a1.name)
print(p1.name)
# #
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
