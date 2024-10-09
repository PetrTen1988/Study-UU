def is_prime(func):
    def wrapper(*args):
        f_result = func(*args)
        count = 1
        num_range = []
        for elem in range(int(f_result)):
            num_range.append(count)
            count += 1
        for i in range(1, int(f_result)):
            if f_result == num_range[i]:
                print('Простое')
                break
            elif f_result % num_range[i] == 0:
                print('Составное')
                break
        return f_result
    return wrapper

@is_prime
def sum_three(*args):
    summ = sum(args)
    return summ

result = sum_three(2, 3, 6)
print(result)
