class Vehicle:

    __color_variants = ('Black', 'White', 'Green')

    def __init__(self, owner, model, color, engine_power, new_color = ''):    ## new_color as empty to avoid positional argument error
        self.owner = owner
        self._model = model
        self._engine_power = engine_power
        self._color = color


    def print_info(self):
        print(f'Model: {self._model} \n'
              f'Engine power: {self._engine_power}\n'
              f'Color: {self._color}\n'
              f'Owner: {self.owner}')

    def get_model(self):
        print(f'Model: {self._model}')

    def get_horsepower(self):
        print(f'Engine power: {self._engine_power}')

    def get_color(self):
        print(f'Color: {self._color}')
        self.color = new_color
        return new_color

    def set_color(self, new_color):

        if new_color.lower() in list(map(str.lower, self.__color_variants)):
            self._color = new_color
        else:
            print(f"You can't change color to {self._color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()







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

