names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya','Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel','Ilya', 'Alexandra']
import random
import time
import multiprocessing


def name():

    b = len(names)
    for i in range(len(names)):

        name = random.randint(0, b - 1)
        time.sleep(1)
        print(names[name])
        print('поел(поела)')

def number():

    for i in range(len(names)):
        number = random.randint(0, 10)

        print('\nномер столика ', number + 1)
        time.sleep(1)

if __name__ == '__main__':
    th1 = multiprocessing.Process(target=name)
    th2 = multiprocessing.Process(target=number)
    th1.start()
    th2.start()