import math
n = float(input())
base = input()

def giv_log(number, base):
    if base == "natural":
        return print(f"{math.log(number):.2f}")
    else:
        base = float(base)
        return print(f"{math.log(number,base):.2f}")

giv_log(n, base)