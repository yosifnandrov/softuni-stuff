from collections import defaultdict

dict = defaultdict(list)

number_of_students = int(input())

for _ in range(number_of_students):
    name, grade = input().split()
    dict[name].append(float(grade))

for student, grades in dict.items():
    grades_str = " ".join(map(lambda f:format(f, '.2f'), grades))
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {grades_str} (avg: {avg_grade:.2f})")

