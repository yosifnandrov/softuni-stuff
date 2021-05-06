numbers = input().split()
new_stack = []

while len(numbers) > 0 :
    new_stack.append(numbers.pop())

print(' '.join(new_stack))
