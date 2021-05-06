tasks = input()
coffees = 0
valid_tasks = ["cat","dog","coding","movie"]
while not tasks == "END":
    is_upper = False
    if tasks.isupper():
        is_upper = True
    if tasks.lower() in valid_tasks:
        if is_upper:
            coffees += 2
        else:
            coffees += 1
    tasks = input()
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)

