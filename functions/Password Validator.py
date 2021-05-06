password = input()
def is_password_valid(password):
    counter_digits = 0
    is_valid = True
    is_symbol = False
    for n in password:
        if n.isdigit() or n.isalpha():
            is_symbol = False
        else:
            is_symbol = True
            break
        if n.isdigit():
            counter_digits += 1
    if is_symbol:
        print(f'Password must consist only of letters and digits')
        is_valid = False
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if counter_digits < 2:
        print(f"Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print(f"Password is valid")

is_password_valid(password)
