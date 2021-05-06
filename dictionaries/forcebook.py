some_input = input()
side_dict = {}
def add_user(my_dict,side_to_join,user_to_add):
    for side, users in my_dict.items():
        if user_to_add in users:
            return my_dict
    if side_to_join not in my_dict:
        my_dict[side_to_join] = []
        my_dict[side_to_join].append(user_to_add)
    else:
        if user_to_add not in my_dict[side_to_join]:
            my_dict[side_to_join].append(user_to_add)
    return my_dict

def transfer_user(my_dict,side_to_transfer,user_to_transfer):
    new_user = True
    for side, users in my_dict.items():
        if user_to_transfer in users:
            my_dict[side].remove(user_to_transfer)
            new_user = False
            add_user(my_dict, side_to_transfer, user_to_transfer)
            print(f"{user_to_transfer} joins the {side_to_transfer} side!")
    if new_user:
        add_user(my_dict, side_to_transfer, user_to_transfer)
        print(f"{user_to_transfer} joins the {side_to_transfer} side!")



while not some_input == "Lumpawaroo":
    some_input = some_input.split()
    not_in = True
    if some_input[1] == "|":
        some_input = " ".join(some_input)
        side, user = some_input.split(" | ")
        add_user(side_dict, side, user)
    else:
        some_input = " ".join(some_input)
        user, side = some_input.split(" -> ")
        transfer_user(side_dict, side, user)
    some_input = input()
side_dict = dict(sorted(side_dict.items(), key=lambda x: (-len(x[1]),x[0])))
for sides, heroes in side_dict.items():
    if len(side_dict[sides]) > 0:
        print(f"Side: {sides}, Members: {len(side_dict[sides])}")
    for h in sorted(side_dict[sides], key=lambda x: x[0]):
        print(f"! {h}")








