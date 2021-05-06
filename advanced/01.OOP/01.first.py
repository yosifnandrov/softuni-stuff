def print_rhombus(n: int):
    GROWING: int = 1
    SHRINKING: int = -1
    def print_line(i:int, direction: int):
        if i == 0:
            return
        line = " " * (n-i) + "* " * i
        print(line.rstrip())
        if i == n:
            direction = SHRINKING
        print_line(i + direction, direction)
    print_line(1, GROWING)

print_rhombus(int(input()))