my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
new_list = []                       # Empty list

while index < len(my_list):
    if my_list[index] == 0:
        index = index + 1
    elif my_list[index] < 0:
        index = index + 1
        break                       # Stop the script when first number below zero occurs
    elif my_list[index] > 0:
        new_list.append(my_list[index])
        index = index + 1
print(new_list)

