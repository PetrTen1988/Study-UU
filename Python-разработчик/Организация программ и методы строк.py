my_string = input()
print(len(my_string)) # to calculate all symbols
print(len(my_string) - my_string.count(' ')) # to calculate symbols except spaces
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', '')) # remove all spaces not only on ends
print(my_string[0])
print(my_string[-1]) # or through index calculation print(my_string[len(my_string)-1])
