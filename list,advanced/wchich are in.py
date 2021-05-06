first_list = input().split(", ")
second_list = input().split(", ")
new_list = [n for n in first_list for l in second_list if n in l]
# for n in first_list:
#     for l in second_list:
#         if n in l:
#             if n in new_list:
#                 continue
#             new_list.append(n)

print(sorted(set(new_list), key=new_list.index))
