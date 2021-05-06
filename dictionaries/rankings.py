from operator import itemgetter


legit = input()
legit_dict = {}
final_dict = {}
partial_dict = {}
total_points = {}

def is_valid(some_dict, contest, password):
    for cont,pasw in some_dict.items():
        if cont == contest:
            if pasw == password:
                return True

points_list = []
def add_points(pnts, usr, old_dict,total_dict,cont,my_list):
    for n, c in old_dict.items():
        for i in range(len(c)):
            for key in c[i]:
                if n not in total_dict:
                    total_dict[n] = int(c[i][key])
                    my_list.append(key)
                    my_list.append(c[i][key])
                else:
                    total_dict[n] += int(c[i][key])
                    my_list.append(key)
                    my_list.append(c[i][key])
        my_list.append(n)
    return total_dict





def save_user(new_dict,contest,points,small_dict,user):
    small_dict = {}
    small_dict[contest] = points
    if user not in new_dict:
        new_dict[user] = [small_dict]
        return new_dict
    for i in range(len(new_dict[user])):
        if contest in new_dict[user][i]:
            if int(new_dict[user][i][contest]) > int(small_dict[contest]):
                return new_dict
            else:
                new_dict[user] = small_dict
                return new_dict

    new_dict[user].append(small_dict)
    return new_dict



while not legit == "end of contests":
    contest,password = legit.split(":")
    legit_dict[contest] = password
    legit = input()

all_information = input()

while not all_information == "end of submissions":
    race, pasw, user, points = all_information.split("=>")
    validation = is_valid(legit_dict,race,pasw)
    if validation:
        final_dict = save_user(final_dict,race,points,partial_dict,user)
    all_information = input()
    if all_information == "end of submissions":
        total_points = add_points(points,user,final_dict,total_points,race,points_list)


a = 0
for name, total in total_points.items():
    if total > a:
        a = total
        b = str(f"Best candidate is {name} with {total} points")
print(b)

# for n, val in final_dict.items():
#     for i in range(len(val)):
#         for con in final_dict[n][i]:

           #numbers.append(final_dict[n][i][con])


#final_dict = dict(sorted(final_dict.items(), key=lambda x: x[1][1]))
final_dict = dict(sorted(final_dict.items(), key = lambda x: (x[0])))


for name,cont_points in final_dict.items():
    print(name)
    for diction in cont_points:
        for k, vel in diction.items():
            cont_points = sorted(cont_points, key = lambda x: x[int(vel)])
            for dic in cont_points:
                for key, value in sorted(dic.items(), key=lambda x:x[1],reverse=True):
                    print(value)
                #print(f"# {cont}->{cont_points[i][cont]}")


