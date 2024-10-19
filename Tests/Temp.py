import time
def run(name, power):
    enemy_power = 100
    count = 0
    print(f'{name}, На нас напали!')
    while enemy_power > 0:
        count += 1
        enemy_power -= int(power)
        time.sleep(1)
        print(f'{name} сражается {count}... Осталось {enemy_power}')
    else:
        print(f'{name} одержал победу спустя {count} дней')


first_knight = run('Sir Lancelot', 10)




 # class MyRange:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         current = self.current
#         self.current += 1
#         return current
#
# # Example usage
# my_range = MyRange(1, 5)
# for num in my_range:
#     print(num)  # Output: 1, 2, 3, 4

# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']
#
# first_result = [len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b)]
# second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
#
# result = []
# for i in range(len(first)):
#     for j in range(len(second)):
#         if len(first[i]) != len(second[i]):
#             result.append(len(first[i]) - len(second[i]))
#             break
#
# print(list(first_result))
# print(list(second_result))


# class WordsFinder:
#     def __init__(self, *args):
#         self.file_names = args
#
#     def get_all_words(self):
#         all_words = {}
#         for name in self.file_names:
#             with open(name) as file:
#                 list_of_words = []
#                 rslt = {}
#                 for line in file:
#                     exclude = [',', '.', '=', '!', '?', ';', ':', ' - ']
#                     tmp_w = ''.join(ch for ch in line if ch not in exclude)
#                     tmp_str = tmp_w.split(' ')
#                     for words in tmp_str:
#                         if words.endswith('\n'):
#                             words = words[:-1]
#                             list_of_words.append(words.lower())
#                         else:
#                             list_of_words.append(words.lower())
#
#                     rslt[name] = list_of_words
#                     all_words.update(rslt)
#         return all_words
#
#     def find(self, word):
#         output = {}
#         self.word = word
#         wrd = word.lower()
#         list_of_files = list(self.file_names)
#         list_to_search = self.get_all_words()
#         for name in list_of_files:
#             tmp = {}
#             tmp2 = {}
#             if wrd in list_to_search[name]:
#                 for_dict = list(list_to_search[name])
#                 tmp[name] = for_dict.index(wrd) + 1
#                 output.update(tmp)
#             else:
#                 tmp2[name] = (f'There is no "{wrd}" in file "{name}"')
#                 output.update(tmp2)
#         return  output
#
#     def count(self,word):
#         output = {}
#         self.word = word
#         wrd = word.lower()
#         list_of_files = list(self.file_names)
#         list_to_search = self.get_all_words()
#         for name in list_of_files:
#             tmp = {}
#             tmp2 = {}
#             count = 0
#             for elem in list_to_search[name]:
#                 if elem == wrd:
#                     count += 1
#                     tmp[name] = f'Word "{wrd}" was met in file "{name}" {count} times.'
#                     output.update(tmp)
#                 else:
#                     tmp2[name] = f'There is no word "{wrd}" in file "{name}".'
#                     output.update(tmp2)
#         return output
#
#
#
# finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# class Vehicle:
#
#     __color_variants = ('Black', 'White', 'Green')
#
#     def __init__(self, owner, model, color, engine_power, new_color = ''):    ## new_color as empty to avoid positional argument error
#         self.owner = owner
#         self._model = model
#         self._engine_power = engine_power
#         self._color = color
#
#
#     def print_info(self):
#         print(f'Model: {self._model} \n'
#               f'Engine power: {self._engine_power}\n'
#               f'Color: {self._color}\n'
#               f'Owner: {self.owner}')
#
#     def get_model(self):
#         print(f'Model: {self._model}')
#
#     def get_horsepower(self):
#         print(f'Engine power: {self._engine_power}')
#
#     def get_color(self):
#         print(f'Color: {self._color}')
#         self.color = new_color
#         return new_color
#
#     def set_color(self, new_color):
#
#         if new_color.lower() in list(map(str.lower, self.__color_variants)):
#             self._color = new_color
#         else:
#             print(f"You can't change color to {self._color}")
#
#
# class Sedan(Vehicle):
#     __PASSENGERS_LIMIT = 5
#
# vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
#
# # Изначальные свойства
# vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
# vehicle1.set_color('Pink')
# vehicle1.set_color('BLACK')
# vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
# vehicle1.print_info()







# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name
#
#     def read_odometer(self):
#         print(f'This car has {self.odometer_reading} miles on it')
#
#     def update_odometer(self, milage):
#         if milage >= self.odometer_reading:
#             self.odometer_reading = milage
#         else:
#             print("You can't roll back an odometer!")
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#
# my_tesla = ElectricCar('Tesla', "Model S", 2022)
# print(my_tesla.get_descriptive_name())
#
#
#
#















# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
# ex = Example('data', second=25, third=3.14)

