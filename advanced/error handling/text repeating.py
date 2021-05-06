text = input()

try:
    times = int(input())
    print(text * times)
except ValueError:
    print("valiable times must be an integer")