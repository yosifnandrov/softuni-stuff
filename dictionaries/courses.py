stud_info = input()
courses_dict = {}
while not stud_info == "end":
    course_name,student_name = stud_info.split(" : ")
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    stud_info = input()

my_dict = sorted(courses_dict.items(), key=lambda l: len(l[1]),reverse=True)
for i in range(len(my_dict)):
    for index in range(0,len(my_dict[i]),2):
        print(f"{my_dict[i][index]}: {len(my_dict[i][index +1])}")
        for x in sorted(my_dict[i][index + 1], key =lambda x:x[0]):
            print(f"-- {x}")