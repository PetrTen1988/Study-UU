def print_parameters(*args, a = '', b = '', c = ''):
    print(*args, a, b, c)

print_parameters(a = 123, b = 'string', c = True )
print_parameters(b = 25)
print_parameters(c = [1, 2, 3])
print_parameters()
print_parameters(1, 2, 3, 5, a = 33, b = False, c = ['q', 2, 54])

values_list = [14, True, 'word']
values_dict = {'a' : 1, 'b' : 'str', 'c' : True}

print_parameters(*values_list)
print_parameters(**values_dict)

values_list2 = [54.32, 'String']

print_parameters(*values_list2, 42)
