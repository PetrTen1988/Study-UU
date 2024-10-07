class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step = 1):
        self.start, self.stop, self.step = start, stop, step
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        if not isinstance(self.stop, int):
            raise StepValueError('stop: некорректный тип данных')
        if not isinstance(self.start, int):
            raise StepValueError('start: некорректный тип данных')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration
        elif self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()