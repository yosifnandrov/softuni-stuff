factor = int(input())
count = int(input())
new = ""
for i in range(factor, (count * factor) + 1, factor):
    x = i
    x = str(x)
    new += x + " "
new_list = new.split()
for one in range(len(new_list)):
    new_list[one] = int(new_list[one])
print(new_list)