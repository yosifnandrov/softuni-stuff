notes = input()
to_do_list = [0] * 10
while not notes == "End":
    importance, task = notes.split("-")
    importance = int(importance)
    for n in range(10, -1, -1):
        if n == importance:
            to_do_list.insert(n, task)
            break
    notes = input()
to_do_list = [x for x in to_do_list if not x == 0]
print(to_do_list)
