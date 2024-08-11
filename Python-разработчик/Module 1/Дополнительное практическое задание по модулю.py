print('Option 1. Iterating over elements')
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg_grades = []     #Empty list for average grades creation
for elem in grades:
    avg_grades.append(sum(elem) / len(elem))    #Average grade calculation for each element. Then add to the list over append
output = dict(zip(sorted(students), avg_grades))    #new dictionary creation. Keys and values connection over zip. list of students sorted
print(output)
