name_id = input()
companies_stats = {}
while not name_id == "End":
    name, id = name_id.split(" -> ")
    id_list = []
    id_list.append(id)
    if name not in companies_stats:
        companies_stats[name] = id_list
    else:
        if id not in companies_stats[name]:
            companies_stats[name].append(id)
    name_id = input()

final_list = sorted(companies_stats.items(), key=lambda x: x[0])
for word, ids in final_list:
    print(word)
    for company, number in companies_stats.items():
        for i in range(len(number)):
            if company == word:
                print(f"-- {number[i]}")


