
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.__module = model
        self.__engine_power = engine_power
        self.__color = color
        self.owner = owner


    def get_model(self): #  возвращает строку: "Модель: <название модели транспорта>"
        return print(f'Модель:{self.__module}')
    def get_horsepower(self): # возвращает строку: "Мощность двигателя: <мощность>"
        return print(f'Мощность двигателя:{self.__engine_power}')
    def get_color(self): # возвращает строку: "Цвет: <цвет транспорта>"
        return print(f'Цвет:{self.__color}')
    def print_info(self): # распечатывает результаты методов (в том же порядке):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Aleksander'

# Проверяем что поменялось
vehicle1.print_info()

# шеф все пропало! гипс снимают клиент уезжает