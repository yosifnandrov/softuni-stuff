first_line = input().split()
palindrome = input()
counter = 0
new_list = []

for word in first_line:
    if word == palindrome:
        counter += 1
    if word == word[::-1]:
        new_list.append(word)
print(new_list)
print(f"Found palindrome {counter} times")