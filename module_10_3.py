import threading
import random
from time import sleep

class Bank:
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        print(f'На депозите {self.balance} средств')
        for i in range(100):
            operation = random.randint(50, 500)
            print(f'\nПополнение: {operation} Баланс: {self.balance}')

            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance += operation
                print(f'\nПополнен: {operation} Баланс: {self.balance}')
            sleep(0.2)

    def take(self):
        for i in range(100):
            operation = random.randint(50, 500)
            print(f'\nЗапрос на {operation}')

            if operation <= self.balance:
                self.balance = self.balance - operation
                print(f'Снятие: {operation} Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.2)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
