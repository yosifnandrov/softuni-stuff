targets = input()
targets_dict = {}
while not targets == "Sail":
    city,population,gold = targets.split("||")
    population = int(population)
    gold = int(gold)
    if city in targets_dict:
        targets_dict[city][0] += population
        targets_dict[city][1] += gold
    else:
        targets_dict[city] = [population,gold]

    targets = input()

events = input()

while not events == "End":
    events = events.split("=>")
    if len(events) == 4:
        command, town, people, cash = events
        people = int(people)
        cash = int(cash)
        targets_dict[town][0] -= people
        targets_dict[town][1] -= cash
        print(f"{town} plundered! {cash} gold stolen, {people} citizens killed.")
        if targets_dict[town][0] <= 0 or targets_dict[town][1] <= 0:
            targets_dict.pop(town)
            print(f"{town} has been wiped off the map!")
    else:
        command, town, cash = events
        cash = int(cash)
        if cash < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            targets_dict[town][1] += cash
            print(f"{cash} gold added to the city treasury. {town} now has {targets_dict[town][1]} gold.")

    events = input()

print(f"Ahoy, Captain! There are {len(targets_dict)} wealthy settlements to go to:")
targets_dict = dict(sorted(targets_dict.items(), key = lambda x:x[0]))
targets_dict = dict(sorted(targets_dict.items(), key = lambda x:x[1][1],reverse=True))
for city,pop_gold in targets_dict.items():
    print(f"{city} -> Population: {pop_gold[0]} citizens, Gold: {pop_gold[1]} kg")


