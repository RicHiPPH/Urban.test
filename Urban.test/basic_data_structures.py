students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]
students_sort = sorted(students)
s = {}
for i, students in enumerate(students_sort):
    s[students] = sum(grades[i]) / len(grades[i])

print(s)