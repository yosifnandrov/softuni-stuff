numbers = [int(el) for el in input().split(", ")]
positives = []
negatives = []
even = []
odd = []
for i in range(len(numbers)):
    if numbers[i] >= 0:
        positives.append(numbers[i])
    else:
        negatives.append(numbers[i])
    if numbers[i] % 2 == 0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print(f"Positive: {', '.join([str(num) for num in positives])}")
print(f"Negative: {', '.join([str(num) for num in negatives])}")
print(f"Even: {', '.join([str(el) for el in even])}")
print(f"Odd: {', '.join([str(num) for num in odd])}")
