


class Horse:

    def __init__(self):
        super().__init__()

        self.x_distance = 0
        self.sound = 'Frrr'


    def run(self, dx):
        self.x_distance += dx

class Eagle:

    def __init__(self):
        super().__init__()
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Eagle, Horse):

    def __init__(self):
        super().__init__()


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'{self.sound}')

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
