number = int(input())
positives_list = []
negative_list = []
for _ in range(number):
    current_number = int(input())
    if current_number >= 0:
        positives_list.append(current_number)
    else:
        negative_list.append(current_number)
print(positives_list)
print(negative_list)
print(f"Count of positives: {len(positives_list)}. Sum of negatives: {sum(negative_list)}")

