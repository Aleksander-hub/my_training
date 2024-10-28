class Animal:
    alive = True #живой
    fed = False #накормленный
    name = ''

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False #съедобность
    name = ''

    def __init__(self, nane):
        self.name = nane


class  Mammal(Animal):

    def eat(self, name):
        self.name = name
        return f'{self.name}'

class Predator(Animal):

    def eat(self, name):
        self.name = name
        return f'{self.name}'

class Flower(Plant):

    def eat(self, food):
        self.food = food
        return f'{self.food}'

class Fruit(Plant):

    def eat(self, food):
        self.food = food
        return f'{self.food}'



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)

print(a1.alive) #True
print(a2.fed) #Fols

print(a1.name, ' не стал есть ', p1.name)
print(a2.name, ' съел ', p2.name)

print(a2.fed) #Fols
print(a1.alive) #True