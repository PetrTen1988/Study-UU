first = ['Strings', 'Student', 'Computers', None]
second = ['Строка', 'Урбан', 'Компьютер', '123']

first_result = [len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b)]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(list(first_result))
print(list(second_result))



