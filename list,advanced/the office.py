given_list = input().split()
happiness_factor = int(input())
given_list = [int(x) for x in given_list]
given_list = [x * happiness_factor for x in given_list]
counter = 0
for num in given_list:
    if num >= sum(given_list) / len(given_list):
        counter += 1
if counter >= len(given_list) / 2:
    print(f"Score: {counter}/{len(given_list)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(given_list)}. Employees are not happy!")
