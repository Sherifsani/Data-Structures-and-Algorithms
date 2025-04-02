students = []

# Input student names and grades
for _ in range(int(input())):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Extract unique grades and sort them
unique_grades = sorted(set(grade for _, grade in students))

# Second lowest grade
second_lowest_grade = unique_grades[1]

# Collect names of students with the second lowest grade
names = sorted([name for name, grade in students if grade == second_lowest_grade])

# Print names alphabetically
for name in names:
    print(name)
