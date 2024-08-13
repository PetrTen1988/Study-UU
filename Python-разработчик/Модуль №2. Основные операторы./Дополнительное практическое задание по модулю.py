string = ''
n = 9
for i in range(1, n):
    for j in range(i + 1, n):
            if n % (i + j) == 0:
                string = string + str(i) + str(j)


print(string)



