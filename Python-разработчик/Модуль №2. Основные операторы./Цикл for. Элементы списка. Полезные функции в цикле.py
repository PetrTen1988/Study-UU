numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
            if numbers[i] == numbers[j]:
                is_primes = True
                # primes.append(numbers[i])
                break
            elif numbers[i] % numbers[j] == 0:
                is_primes = False
                # not_primes.append(numbers[i])
                break
    if is_primes:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('primes', primes)
print('not primes', not_primes)

