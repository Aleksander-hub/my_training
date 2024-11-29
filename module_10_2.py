
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name} на нас напали! Кто? Супостаты!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1
            if self.enemies < 0:
                self.enemies = 0
            else:
                print(f"{self.name} мочилово {self.days} день(дней)..., осталось {self.enemies} битв.")
        print(f"{self.name} одержал победу {self.days} день(дней)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы завершены! Всех убили")
# Бабе цветы, детям мороженное




