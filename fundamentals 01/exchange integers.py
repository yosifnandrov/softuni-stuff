a = int(input())
b = int(input())
print(f"Before:\na = {a}\nb = {b}")
l = a
a = b
b = l
print(f"After:\na = {a}\nb = {b}")