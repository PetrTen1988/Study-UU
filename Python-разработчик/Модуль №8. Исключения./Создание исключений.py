class IncorrectVinNumber(Exception):
    def __init__(self, message, *args):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message, *args):
        self.message = message

class Car:
    def __init__(self, model, vin, plate):
        self.model = model
        self.__vin = vin
        self.__plate = plate
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_number(plate):
            self.__plate = plate

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber ("Некорректный тип vin номер")
        elif vin not in range(1000000, 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_number(self, plate):
        if not isinstance(plate, str):
            raise IncorrectCarNumber ("Некорректный тип данных для номеров")
        elif len(plate) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')






