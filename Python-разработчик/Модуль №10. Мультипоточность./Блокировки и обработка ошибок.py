import time
import threading
from threading import Lock
from random import randint

global balance

class Bank:
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = threading.Lock()
        self.not_on_time_exec = 0


    def deposit(self):
        for i in range(100):
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()

            self.lock.acquire()
            summ = randint(50, 300)
            self.balance += summ
            print(f'Пополнение: {summ}. Баланс: {self.balance}')
            time.sleep(0.01)
            self.lock.release()

    def take(self):
        for i in range(100):
            self.lock.acquire()
            summ = randint(50, 500)
            print(f'Запрос на снятие {summ}')
            if self.balance >= summ:
                self.balance -= summ
                print(f'Снятие: {summ}. Баланс: {self.balance}')
                time.sleep(0.001)
                self.lock.release()
            else:
                print(f'Запрос отклонен, недостаточно средств')
                time.sleep(0.001)
                self.lock.acquire()
            # self.lock.release()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
