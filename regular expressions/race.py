import re

players = input().split(",")
coded_msg = input()
players_dict = {}
players = [el.strip() for el in players]
final_list = []
for player in players:
    players_dict[player] = 0
while not coded_msg == "end of race":
    pattern_name = r"[A-Za-z]+"
    found_name = re.findall(pattern_name, coded_msg)
    full_name = "".join(found_name)
    if full_name in players:
        pattern_nums = r"\d"
        numbers = re.findall(pattern_nums,coded_msg)
        numbers = [int(el) for el in numbers]
        players_dict[full_name] += sum(numbers)
    coded_msg = input()
players_dict = dict(sorted(players_dict.items(), key=lambda x:x[1],reverse=True))

for name,dist in players_dict.items():
    final_list.append(name)

for i in range(len(final_list)):
    print(f"1st place: {final_list[0]}")
    print(f"2nd place: {final_list[1]}")
    print(f"3rd place: {final_list[2]}")
    break








