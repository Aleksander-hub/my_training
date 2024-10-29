class Animal:
    alive = True #живой
    fed = False #накормленный
    name = ''

    def __init__(self, name):
        self.name = name

    def eat(self, food):

        if food.edible:
            print(f'{self.name}, съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name}, не стал есть {food.name}')
            self.alive = False



class Plant:
    edible = False #съедобность
    name = ''

    def __init__(self, name):
        self.name = name


class  Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True
    pass



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')



print(a1.name)
print(p1.name)

print(a1.alive) #True
print(a2.fed) #Fols

a1.eat(p1)
a2.eat(p2)


print(a2.fed) #Fols
print(a1.alive) #True
