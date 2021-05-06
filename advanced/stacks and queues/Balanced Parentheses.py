parentheses = input()
stack = []
valid = True
valid_cases = ["[]","{}","()"]
for char in parentheses:
    if char == "(":
        stack.append(char)
    elif char == "[":
        stack.append(char)
    elif char == "{":
        stack.append(char)
    else:
        if not stack.pop()+char in valid_cases:
            print("NO")
            valid = False
            break
if valid:
    print("YES")



