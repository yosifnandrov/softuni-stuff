n = int(input())
odd = set()
even = set()
for i in range(1, n+1):
    sum_letters = 0
    name = input()
    for letter in name:
        sum_letters += ord(letter)
    value = sum_letters // i
    if value % 2 == 0:
        even.add(value)
    else:
        odd.add(value)
if sum(odd) == sum(even):
    union = list(odd.union(even))
    union = [str(el) for el in union]
    print(", ".join(union))
elif sum(odd) > sum(even):
    difference = list(odd.difference(even))
    difference = [str(el) for el in difference]
    print(", ".join(difference))
else:
    symmetric_diff = list(odd.symmetric_difference(even))
    symmetric_diff = [str(el) for el in symmetric_diff]
    print(", ".join(symmetric_diff))