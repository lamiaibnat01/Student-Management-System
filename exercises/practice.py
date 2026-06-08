from modules.grades import calculate_grade

marks = [85, 72, 66, 58, 40]

for mark in marks:
    print(mark, "->", calculate_grade(mark))
