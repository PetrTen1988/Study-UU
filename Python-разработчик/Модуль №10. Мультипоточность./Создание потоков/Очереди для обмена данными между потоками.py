from queue import Queue
from random import randint
from threading import Thread
import time

q = Queue(maxsize=6)

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        self.name = name

    def run(self):
        time.sleep(randint(3,10))

class Cafe:
    def __init__(self, tables, queue):
        self.guests = None
        self.tables = tables
        self.queue = queue

    def guest_arrival(self, *guests):
        self.guests = [Guest(name) for name in guests_names]
        for guests in guests_names:
            q.put(guests)
            print(f'{guests} сел(-а) за стол номер {tables}')





tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

