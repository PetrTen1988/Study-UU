import os
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(ROOT):
    count = 0
    for file in files:
        file_path = os.path.join(ROOT,file)
        file_time = time.ctime(os.path.getctime(file_path))
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(file)))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        count += 1
        print('-------------------------File #', count, '----------------------------------------------')
        print(f'Обнаружен файл: {file}\nПуть: {file_path}\nРазмер: {file_size} байт\nВремя изменения: {formatted_time}\nРодительская директория: {parent_dir}\n')
        print(f'Всего файлов: {count}')

