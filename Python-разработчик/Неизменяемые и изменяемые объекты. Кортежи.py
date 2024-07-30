immutable_var = (1, 123, '23', True)
print(immutable_var)
#immutable_var.remove(123) - turple can't be changed. It's immutable list (constant)
mutable_var = [1, True, 'string', 18]
del mutable_var[0] #first element deleted
print(mutable_var)
mutable_var.append('last_var') #element added to the end of the list
print(mutable_var)
mutable_var.insert(1, 'second_var') #element inserted at 2nd place (list index 1)
print(mutable_var)
third_var = mutable_var.pop(2) #removed third element from the list
print(mutable_var)
print(third_var, type(third_var)) #poped element returned
