integers = input().split(", ")

def palindrome(integers):
    for i in integers:
        str_i = str(i)
        if str_i == str_i[::-1]:
            print("True")
        else:
            print("False")
palindrome(integers)
