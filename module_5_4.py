

class House:
    houses_history = 'снесён, но он останется в истории'
    def __new__(cls, *args, **kwargs):
        cls.houses_history = cls.houses_history
        return super().__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def number_of_floors_1(self, number_of_floors):
        print(self.number_of_floors)

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'{self.name}'





    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors


    def __add__(self, value):
        self.number_of_floors += value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.number_of_floors += value
        return self



    def go_to(self, new_floor):
        self.new_floor = new_floor

        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        if new_floor < 1:
            print("Такого этажа не существует")

        a = 1
        for i in range(new_floor ):
            print(a, 'этаж')
            a += 1


h1 = House('ЖК Эльбрус', 10)
print(h1)
h2 = House('ЖК Акация', 20)
print(h1,h2)
h3 = House('ЖК Матрёшки', 20)
print(h1, h2, h3)
print(h2, House.houses_history)
print(h3, House.houses_history)
print(h1, h2, h3)
print(h1, House.houses_history)
# Удаление объектов
del h2
del h3

# 'шеф все пропало!, гипс снимают, клиент уезжает!'
