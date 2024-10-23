from encodings.punycode import selective_find


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def number_of_floors_1(self, number_of_floors):
        print(self.number_of_floors)

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}:{self.number_of_floors} этажей'





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
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1.__add__(10)# __add__
print(h1)
print(h1 == h2)

h1.__iadd__(10) # __iadd__
print(h1)

h2.__radd__(10) # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__





#h1.go_to(5)
#h2.go_to(10)

# 'шеф все пропало!, гипс снимают, клиент уезжает!'
# __________