user_names = input().split(", ")

valid_names = []
for names in user_names:
    is_valid = False
    if 3 <= len(names) <= 16:
        for symbol in names:
            if symbol.isalpha() or symbol.isdigit() or "_" in symbol or "-" in symbol:
                is_valid = True
            else:
                is_valid = False
                break
        if is_valid:
            valid_names.append(names)

for valid_name in valid_names:
    print(valid_name)
