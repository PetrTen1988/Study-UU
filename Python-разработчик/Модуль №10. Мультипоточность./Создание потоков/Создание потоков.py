from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):

    with open(file_name, 'a') as file:
        start_time = datetime.now()
        count = 0
        for i in range(word_count):
            count += 1
            file.write(f"Какое-то слово №: {count}\n")
        end_time = datetime.now()
        res = end_time - start_time
        print(f'All words in {file_name} recorded in {res} seconds')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

print('----------------------------------------------------------')

thr_one = Thread(target=write_words, args=(10, 'example5.txt'))
thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
thr_three = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

thr_one.start()
thr_two.start()
thr_three.start()
thr_four.start()

thr_one.join()
thr_two.join()
thr_three.join()
thr_four.join()