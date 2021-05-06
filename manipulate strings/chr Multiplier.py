two_strings = input().split()
numbers = []

for word in two_strings:
    for char in word:
        numbers.append(ord(char))
first = numbers[:len(two_strings[0]):]
second = numbers[len(two_strings[0]):]

if len(first) == 0:
    print(sum(second))
elif len(second) == 0:
    print(sum(first))
else:
    result = 0
    for i in range(len(first)):
        for ind in range(len(second)):
            if i == ind:
                result += first[i] * second[ind]
            if i >= len(second):
                result += first[i]
                break
            elif ind >= len(first):
                result += second[ind]
    print(result)





