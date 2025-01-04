import time
import asyncio

async def start_strongman_1(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(1, power + 1):
        await asyncio.sleep(1)
        print(f'Силач {name} поднял {i} шар')
    print(f"Силач {name} закончил соревнования")

async def start_strongman_2(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(1, power + 1):
        await asyncio.sleep(2)
        print(f'Силач {name} поднял {i} шар')
    print(f"Силач {name} закончил соревнования")

async def start_strongman_3(name, power):
    print(f"Силач {name} начал соревнования")
    for i in range(1, power + 1):
        await asyncio.sleep(3)
        print(f'Силач {name} поднял {i} шар')
    print(f"Силач {name} закончил соревнования")

async def start_tournament():

    task1 = asyncio.create_task(start_strongman_1('Pasha', 3))
    task2 = asyncio.create_task(start_strongman_2('Denis', 4))
    task3 = asyncio.create_task(start_strongman_3('Apollon', 5))
    await task1
    await task2
    await task3


if __name__ == "__main__":
    asyncio.run(start_tournament())



