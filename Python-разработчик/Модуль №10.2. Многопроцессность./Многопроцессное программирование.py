import multiprocessing
import time

file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

#  --------Linear mode--------------
def read_info():
    all_data = []
    t0 = time.time()
    for name in file_names:
        with open(name, 'r') as file:
            for line in file:
                all_data.append(line)
    t1 = time.time()
    t_res = t1 - t0
    print(f'Execution time of {file_names} in linear mode is {t_res} sec')



# -------------Multiprocessing mode--------------------
def read_info_multi():
    all_data_multi = []
    for name in file_names:
        with open(name, 'r') as file:
            for line in file:
                all_data_multi.append(line)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        t0 = time.time()
        pool.map_async(read_info_multi(), file_names)
        t1= time.time()
        print(f'Execution time of {file_names} in Multiprocessing mode is {t1 - t0} sec')



read_info()



