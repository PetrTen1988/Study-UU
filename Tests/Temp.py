count_digits = "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"

count = 0
for elem in range(len(count_digits)):
    if isinstance(int(elem), int):
        count += elem
print(count)
