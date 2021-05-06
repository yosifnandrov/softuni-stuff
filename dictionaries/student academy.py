from statistics import mean
rows = int(input())
students_dict = {}
for n in range(rows):
    grades = []
    name = input()
    grade = float(input())
    grades.append(grade)
    if name not in students_dict:
        students_dict[name] = grades.copy()
    else:
        students_dict[name].append(grade)
average_dict = students_dict.copy()
for n,g in students_dict.items():
    if mean(g) < 4.5:
        average_dict.pop(n)
    else:
        average_dict[n] = mean(g)

average_dict = sorted(average_dict.items(), key= lambda x:x[1],reverse = True)

for index in range(len(average_dict)):
    for i in range(0,len(average_dict[index]),2):
        print(f"{average_dict[index][i]} -> {average_dict[index][i+1]:.2f}")



