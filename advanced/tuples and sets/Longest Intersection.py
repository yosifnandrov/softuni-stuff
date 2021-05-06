n = int(input())

max_length = 0
for _ in range(n):
    first_set = set()
    second_set = set()
    first, second = input().split("-")
    start_first, end_first = first.split(",")
    start_first = int(start_first)
    end_first = int(end_first)
    start_second, end_second = second.split(",")
    start_second = int(start_second)
    end_second = int(end_second)
    for i in range(start_first, end_first+1):
        first_set.add(i)
    for ind in range(start_second, end_second+1):
        second_set.add(ind)

    intersection = first_set.intersection(second_set)
    if len(intersection) > max_length:
        max_length = len(intersection)
        max_length_set = intersection

print(f"Longest intersection is {list(max_length_set)} with length {max_length}")
