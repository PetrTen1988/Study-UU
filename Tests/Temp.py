class Horse():
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx


class Eagle():
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.dy = dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
        return [self.x_distance, self.y_distance]

    def get_pos(self):
        return [self.x_distance, self.y_distance]

    def voice(self):
        print(self.sound)




p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()



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

