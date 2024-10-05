def add_everything_up(a, b):
    try:
        rslt = a + b
        return round(rslt, 3)
    except TypeError:
        rslt = str(a) + str(b)
        return rslt

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))