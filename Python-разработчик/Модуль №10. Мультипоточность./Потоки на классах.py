from threading import Thread
import random
import time


class Knight(Thread):

    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power



    def run(self):
        enemy_power = 100
        count = 0
        print(f'{self.name}, На нас напали!')
        while enemy_power > 0:
            count += 1
            enemy_power -= int(self.power)
            print(f'{self.name} сражается {count} дней(дня)... Осталось {enemy_power} врагов')
            time.sleep(random.choice([0.5, 1]))  # добавлен RANDOM.CHOICE так как происходит "склейка" при выводе результатов
        else:
            print(f'{self.name} одержал победу спустя {count} дней(дня)')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

