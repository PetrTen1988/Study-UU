first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# first_result
first_result = []
for elem in first_strings:
    if len(elem) >= 5:
        first_result.append(len(elem))

# second_result
second_result = []
for elem in first_strings:
    for item in second_strings:
        if len(elem) == len(item):
            second_result.append((elem, item))

# third_result
third_result = {}
test_list = first_strings + second_strings
for elem in test_list:
    if len(elem) % 2 == 0:
        third_result[elem] = len(elem)


print(first_result)
print(second_result)
print(third_result)

