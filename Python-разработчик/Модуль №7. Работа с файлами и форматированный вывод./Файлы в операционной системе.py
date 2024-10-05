import os
import time

directory = '/Users/petrten/Documents/GitHub/Study-UU/Python-разработчик/Модуль №7. Работа с файлами и форматированный вывод.'
for root, dirs, files in os.walk(directory):
    count = 0
    for file in files:
        file_path = os.path.join(directory, file)
        file_time = time.ctime(os.path.getctime(file))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(directory)
        count += 1
        print('File #', count)
        print(f'Обнаружен файл: {file}\nПуть: {file_path}\nРазмер: {file_size} байт\nВремя изменения: {formatted_time}\nРодительская директория: {parent_dir}')



