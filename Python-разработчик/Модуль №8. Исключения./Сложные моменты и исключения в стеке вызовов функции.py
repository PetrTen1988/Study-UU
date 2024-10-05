def personal_sum(numbers):
    summ = 0
    incorrect_data = 0
    for elem in numbers:
        try:
            summ += elem
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {elem}')
    return (summ, incorrect_data)

def calculate_average(numbers):
    result = None
    try:
        summ = personal_sum(numbers)[0]
        count = 0
        for elem in numbers:
            if isinstance(elem, int):
                count += 1
        result = summ / count
    except (TypeError, ZeroDivisionError):
        print('В numbers записан некорректный тип данных')
    return result


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать







