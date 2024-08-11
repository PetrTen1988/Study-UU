import random

def get_matrix():                           # - Function with custom n, m and randomly generated values
    m = int(input('Введите число строк '))
    n = int(input('Введите число столбцов '))
    range_start, range_stop = input('Введите диапазон значений: ').split()
    matrix = []
    if n > 0 and m > 0:
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(random.randint(int(range_start), int(range_stop))) # Randomizer of values with ranges
            matrix.append(tmp)
        print('Table form matrix representation:')
        for i in range(len(matrix)): # Matrix output in table form
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = " ")
            print()

        print('List form output: ', matrix) # Matrix output as a list
    else:
        matrix = []
        print(matrix)

# get_matrix()

def get_matrix_1(n, m, value):                           # - Function parameters contorl throuh arguments
    matrix = []
    if n > 0 and m > 0:
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(value)
            matrix.append(tmp)
        print('Table form matrix representation:')
        for i in range(len(matrix)): # Matrix output in table form
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = " ")
            print()

        print('List form output: ', matrix) # Matrix output as a list
    else:
        matrix = []
        print(matrix)

# get_matrix_1(2, 3, 43)

