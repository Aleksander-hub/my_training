class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'Название: {self.name}, количество этожей {self.number_of_floors}')

    def number_of_floors_1(self, number_of_floors):
        print(self.number_of_floors)

    def __len__(self, number_of_floors):
        return self.number_of_floors
    def __str__(self, name):
        return self.name



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

a = 10; b= 20

h1 = House('ЖК Эльбрус', a)
h2 = House('ЖК Акация', b)
h1.number_of_floors_1(a)
h2.number_of_floors_1(b)

#h1.go_to(5)
#h2.go_to(10)

# 'шеф все пропало!, клиент уезжает гипс снимают'