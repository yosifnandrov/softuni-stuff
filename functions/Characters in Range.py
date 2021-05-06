a = input()
b = input()

def ascii_between(a,b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")
ascii_between(a,b)