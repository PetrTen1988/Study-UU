# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

# Замыкание:
def get_advanced_writer(file_name):
    def write_function(*data_set):
        with open(file_name, 'a', encoding = 'utf-8') as file:
            for elem in data_set:
                file.write(str(elem) + '\n')
    return write_function

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
import random
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

