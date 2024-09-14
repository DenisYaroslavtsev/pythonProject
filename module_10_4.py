import queue
import time
from threading import Thread
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            placed = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол № {table.number}')
                    placed = True
                    break

            if not placed:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер: {table.number} свободен')
                        table.guest = None

                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел за стол номер: {table.number}')
                        next_guest.start()
                        time.sleep(1)

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
