def numbers_searching(*args):
    final_list = []
    for i in range(min(args), max(args) + 1):
        if i not in args:
            final_list.append(i)
    duplicates = set()
    args = list(map(str, args))
    for num in args:
        if args.count(num) >= 2:
            duplicates.add(int(num))
    final_list.append(sorted(list(duplicates)))

    return final_list

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))