some_text = input().split(">")
new_list = some_text.copy()
counter = 0
explosion = 0
for index in range(len(some_text)):
    for i in range(len(some_text[index])):
        if some_text[index][i].isdigit():
            explosion += int(some_text[index][i])
            if explosion == 1:
                if len(some_text[index]) > 1:
                    new_list[index] = new_list[index][1::]
                else:
                    new_list.remove(some_text[index][i])
                    new_list.insert(index,"*")
                explosion = 0
            else:
                if explosion > len(some_text[index]):
                    new_range = len(some_text[index])
                    for shortexplo in range(new_range):
                        new_list.remove(some_text[index][shortexplo])
                        counter += 1
                else:
                    new_list[index] = new_list[index][explosion::]
                    explosion = 0
                if len(some_text[index]) == 1:
                    new_list.insert(index,"*")
                explosion -= counter

final_list = ">".join(new_list)
final_list = final_list.replace("*","")
print(final_list)





