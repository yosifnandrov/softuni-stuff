def age_assignment(*args, **kwargs):
    new_dict = {}
    for arg in args:
        for key in kwargs:
            if arg[0] == key:
                new_dict[arg] = kwargs[key]
    return new_dict

print(age_assignment("Peter", "George", G=26, P=19))
