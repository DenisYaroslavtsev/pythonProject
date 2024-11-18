import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    for ball in range(1, 6):
        strength = 1 / power
        await asyncio.sleep(strength)
        print(f'Силач {name} поднял {ball} шар')
    print(f'Силач {name} закончил соревнование')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
