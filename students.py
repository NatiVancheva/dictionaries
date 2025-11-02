students_info = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, id_num, course = info[0], info[1], info[2]
    if course not in students_info:
        students_info[course] = {}
    students_info[course][id_num] = name
    command = input()

course = " ".join(command.split("-"))
for key, value in students_info.items():
    if key == course:
        for id_num, name in value.items():
            print(f'{name} - {id_num}')
