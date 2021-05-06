grade = float(input())

def print_grades_to_words(grade):
    if 2 <= grade <= 2.99:
        print("Fail")
    elif grade <= 3.49:
        print(f"Poor")
    elif grade <= 4.49:
        print("Good")
    elif grade <= 5.49:
        print("Very Good")
    elif grade <= 6:
        print(f"Excellent")


print_grades_to_words(grade)

