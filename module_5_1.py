class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)