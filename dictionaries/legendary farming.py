from operator import itemgetter


my_dict = {}
my_dict["shards"] = 0
my_dict["fragments"] = 0
my_dict["motes"] = 0
is_obtained = False
materials_coming = input().split()
while not is_obtained:
    for i in range(1, len(materials_coming)+1, 2):
        key = materials_coming[i].lower()
        if key not in my_dict:
            my_dict[key] = int(materials_coming[i-1])
        else:
            my_dict[key] += int(materials_coming[i-1])
        if my_dict[key] >= 250:
            is_obtained = True
            my_dict[key] -= 250
            if key == "shards":
                print("Shadowmourne obtained!")
                break
            elif key == "fragments":
                print("Valanyr obtained!")
                break
            elif key == "motes":
                print(f"Dragonwrath obtained!")
                break
    if not is_obtained:
        new_line = input().split()
        materials_coming.clear()
        for word in new_line:
            materials_coming.append(word)
cut_dict = my_dict.copy()
junk_dict = {}
for key, value in my_dict.items():
    if not key == "motes" and not key == "shards" and not key == "fragments":
        cut_dict.pop(key)
        junk_dict[key] = value


if len(list(set(list(cut_dict.values())))) > 2:
    final_dict = dict(sorted(cut_dict.items(), key=lambda x: x[1],reverse=True))
    for item, count in final_dict.items():
        print(f"{item}: {count}")
else:
    final_dict = dict(sorted(cut_dict.items(), key=lambda x: x[0]))
    last_sort = dict(sorted(final_dict.items(), key=lambda x: x[1], reverse=True))
    for material, quantity in last_sort.items():
        print(f"{material}: {quantity}")

junk_tupl = dict(sorted(junk_dict.items(), key=lambda x: x[0]))
for m, q in junk_tupl.items():
    print(f"{m}: {q}")
 

