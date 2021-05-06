import math

students_count = int(input())
lectures = int(input())
additional_bonus = int(input())
student_attendances = []
total = []
for att in range(students_count):
    attendances = int(input())
    student_attendances.append(attendances)
    total.append((attendances / lectures) * (5 + additional_bonus))

def give_me_index(some_list):
    for i in range(len(some_list)):
        if some_list[i] == max(some_list):
            return i


print(f"Max Bonus: {math.ceil(max(total))}.")
print(f"The student has attended {math.ceil(student_attendances[(give_me_index(student_attendances))])} lectures.")


