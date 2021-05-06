from operator import itemgetter


information = input()
list_contests = {}
user_points = {}
user_contests = {}
user_total_points = {}

def check_if_done(user,contest,user_cont_dict,pnts,user_points,total_pnts):
    if user not in user_cont_dict:
        user_cont_dict[user] = [contest]
        user_points[user] = [pnts]
    if user not in total_pnts:
        total_pnts[user] = pnts

    for usr, cont in user_cont_dict.items():
        if usr == user:
            if not contest in cont:
                user_points[user].append(points)
                user_cont_dict[user].append(contest)
                total_pnts[user] += pnts
            else:
                for i in range(len(user_points[user])):
                    if user_points[user][i] < pnts:
                        total_pnts[user] -= user_points[user][i]
                        user_points[user][i] = pnts
                        total_pnts[user] += pnts
    return user_cont_dict



while not information == "no more time":
    user, contest, points = information.split(" -> ")
    points = int(points)
    if contest not in list_contests:
        list_contests[contest] = [user]
    else:
        if user not in list_contests[contest]:
            list_contests[contest].append(user)
    user_contests = check_if_done(user,contest,user_contests,points,user_points,user_total_points)

    information = input()

user_points = dict(sorted(user_points.items(), key = itemgetter(0)))

counter = 0
for cont, users in list_contests.items():
    print(f"{cont}: {len(users)} participants")
    counter = 0
    for usr, points in sorted(user_points.items(), key = itemgetter(1),reverse=True):
        for i in range(len(points)):
            if usr in users:
                counter += 1
                print(f"{counter}. {usr} <::> {points[i]}")
                user_points[usr].remove(points[i])
                break


counter_two = 0
print("Individual standings:")
for u,p in sorted(user_total_points.items(), key = lambda y:y[1],reverse=True):
    counter_two += 1
    print(f"{counter_two}. {u} -> {p}")

