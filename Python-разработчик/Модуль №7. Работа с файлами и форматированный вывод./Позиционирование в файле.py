def custom_write(file_name, strings):
    count = 0
    rslt = {}
    file = open(file_name, 'a', encoding='utf-8')
    for elem in strings:
        pos = file.tell()
        file.write(str(elem) + '\n')
        count += 1
        string_position = (int(count), int(pos))
        rslt[string_position] = elem
    return rslt
    file.close()

open("test.txt", 'w').close()     # to erase file content before next run


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)


for elem in result.items():
    print(elem)