info = input()
name_points = {}
language_submissions = {}


def add_new_user(dict,user,points):
    points = int(points)
    if user not in dict:
        dict[user] = 0
    for u, p in dict.items():
        if points > dict[user]:
            dict[user] = points
            return dict

        return dict


def add_submission(dict,language):
    if language in dict:
        dict[language] += 1
        return dict
    else:
        dict[language] = 1


while not info == "exam finished":
    information = info.split("-")
    if len(information) < 3:
        user,command = info.split("-")
        name_points.pop(user)
    else:
        user,language,points = info.split("-")
        add_new_user(name_points,user,points)
        add_submission(language_submissions,language)
    info = input()

name_points = dict(sorted(name_points.items(),key = lambda x:(-x[1],x[0])))
language_submissions = dict(sorted(language_submissions.items(), key = lambda x: (-x[1],x[0])))
print("Results:")
for name, pnts in name_points.items():
    print(f"{name} | {pnts}")
print(f"Submissions:")
for l, subm in language_submissions.items():
    print(f"{l} - {subm}")


