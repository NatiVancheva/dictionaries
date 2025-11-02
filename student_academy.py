students = {}
number_of_students = int(input())
for _ in range(number_of_students):
    student_name = input()
    grade = float(input())
    if student_name in students:
        students[student_name] = []
    students[student_name].append(grade)
for student_name, grades in students.items():
    average_grades = sum(grades) / len(grades)
    if average_grades >= 4.5:
        print(f"{student_name} -> {average_grades:.2f}")


