text = input()


def give_me_rage_text(some_string):
    for i in range(len(some_string)):
        if some_string[i].isdigit():
            if i + 1 <= len(some_string) - 1:
                if some_string[i+1].isdigit():
                    number = int(some_string[i] + some_string[i+1])
                    rage_text = some_string.replace(some_string[:len(some_string)], (some_string[:i] * number).upper())
                    return rage_text
            else:
                if some_string[i] == "0":
                    rage_text = some_string.replace(some_string[:i+1], "")
                    return rage_text
                else:
                    rage_text = some_string.replace(some_string[i], some_string[:i] * (int(some_string[i]) - 1)).upper()
                    return rage_text
new_list = []
counter = 0
for i in range(len(text)):
    if text[i].isdigit():
        if text[i-1].isdigit():
            continue
        if i+1 <= len(text) - 1:
            if text[i+1].isdigit():
                counter += 1
                if counter == 1:
                    new_list.append(text[:i + 2])
                    last_index = i + 2
                else:
                    new_list.append(text[last_index:i + 2])
                    last_index = i + 2
            else:
                counter += 1
                if counter == 1:
                    new_list.append(text[:i + 1])
                    last_index = i + 1
                else:
                    new_list.append(text[last_index:i + 1])
                    last_index = i + 1

        else:
            counter += 1
            if counter == 1:
                new_list.append(text[:i+1])
                last_index = i+1
            else:
                new_list.append(text[last_index:i+1])
                last_index = i + 1
result = ""
for el in new_list:
    result += give_me_rage_text(el)
print(f"Unique symbols used: {len(set(result))}")
print(result)


