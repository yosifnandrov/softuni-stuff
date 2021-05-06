# dict_indict = {"car": {"opel": "corsa"}}
#
# print(dict_indict["car"]["opel"])

# some_list = [1, 6, 7, 15, 22]
# print(list(reversed(some_list)))
give_me = input()
my_list = give_me.split()
result = ""
palindrom_len = 0
counter = 0
counter_two = 0
list_palindroms = []
for word in my_list:
    for i in range(1,len(word)-1):
        is_palindrom = False
        if word[i] == word[i + 1]:
            right_index = i + 2
            left_index = i - 1
            is_palindrom = True
            counter = 2
            while is_palindrom:
                if right_index not in range(0, len(word)+1) or left_index not in range(0, len(word)+1):
                    break
                if word[right_index] == word[left_index]:
                    right_index += 1
                    left_index -= 1
                    counter += 2
                else:
                    is_palindrom = False
            list_palindroms.append(counter)
        else:
            if word[i+1] == word[i - 1]:
                counter_two = 3
                right_index = i + 2
                left_index = i - 2
                is_palindrom = True
                while is_palindrom:
                    if right_index not in range(0, len(word) + 1) or left_index not in range(0, len(word) + 1):
                        break
                    if word[right_index] == word[left_index]:
                        right_index += 1
                        left_index -= 1
                        counter_two += 2
                    else:
                        is_palindrom = False
                list_palindroms.append(counter_two)

print(max(list_palindroms))
#olebbelka




