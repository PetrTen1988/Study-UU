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

    def get_forsepower(self):
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
    def __init__(self, owner, model, engine_power, color, new_color = ''):     # new_color as empty to avoid positional argument error
        super().__init__(owner, model, engine_power, color, new_color = '')    # new_color as empty to avoid positional argument error

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


