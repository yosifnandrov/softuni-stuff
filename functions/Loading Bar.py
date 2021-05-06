number = int(input())

def loading_bar(number):
    loading_bar_list = []
    l_number = number // 10
    for n in range(1, 11):
        if n > l_number:
            loading_bar_list.append(".")
        else:
            loading_bar_list.append("%")
    loading_bar_str = "".join(loading_bar_list)
    if l_number == 10:
        print(f"{number}% Complete!")
        print(f"[{loading_bar_str}]")
    else:
        print(f"{number}%", end=" ")
        print(f"[{loading_bar_str}]")
        print("Still loading...")

loading_bar(number)