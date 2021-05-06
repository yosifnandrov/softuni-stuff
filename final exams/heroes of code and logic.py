number_of_heroes = int(input())
heroes_dict = {}
for _ in range(number_of_heroes):
    hero_stats = input()
    name, hp, mp = hero_stats.split()
    hp = int(hp)
    mp = int(mp)
    heroes_dict[name] = [hp,mp]

command = input()

while not command == "End":
    command = command.split(" - ")
    if len(command) == 4:
        if "CastSpell" in command:
            cmnd,name,mp_needed,spell_name = command
            mp_needed = int(mp_needed)
            if heroes_dict[name][1] >= mp_needed:
                heroes_dict[name][1] -= mp_needed
                print(f"{name} has successfully cast {spell_name} and now has {heroes_dict[name][1]} MP!")
            else:
                print(f"{name} does not have enough MP to cast {spell_name}!")
        elif "TakeDamage" in command:
            cmnd,name,dmg,attacker = command
            dmg = int(dmg)
            if heroes_dict[name][0] - dmg > 0:
                heroes_dict[name][0] -= dmg
                print(f"{name} was hit for {dmg} HP by {attacker} and now has {heroes_dict[name][0]} HP left!")
            else:
                heroes_dict.pop(name)
                print(f"{name} has been killed by {attacker}!")
    else:
        if "Recharge" in command:
            cmd, name,amount = command
            amount = int(amount)
            if heroes_dict[name][1] + amount > 200:
                recovered_mp = 200 - heroes_dict[name][1]
                heroes_dict[name][1] = 200
                print(f"{name} recharged for {recovered_mp} MP!")
            else:
                heroes_dict[name][1] += amount
                print(f"{name} recharged for {amount} MP!")
        elif "Heal" in command:
            cmd,name,amount_hp = command
            amount_hp = int(amount_hp)
            if heroes_dict[name][0] + amount_hp > 100:
                recovered_hp = 100 - heroes_dict[name][0]
                heroes_dict[name][0] = 100
                print(f"{name} healed for {recovered_hp} HP!")
            else:
                heroes_dict[name][0] += amount_hp
                print(f"{name} healed for {amount_hp} HP!")
    command = input()

heroes_dict = dict(sorted(heroes_dict.items(), key = lambda x:x[0]))
heroes_dict = dict(sorted(heroes_dict.items(), key = lambda x:x[1][0],reverse=True))
for hero_name, hp_mp in heroes_dict.items():
    print(f"{hero_name}")
    print(f"  HP: {hp_mp[0]}")
    print(f"  MP: {hp_mp[1]}")

