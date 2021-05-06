moves = int(input())
total_points = 0
percent_per_move = 1 / moves * 100
percent_less_nine = 0
percent_less_twenty_nine = 0
percent_less_nineteen = 0
percent_less_thirty_nine = 0
percent_less_than_fifty = 0
invalid_numbers = 0
for _ in range(moves):
    current_number = int(input())
    if current_number < 0 or current_number > 50:
        total_points /= 2
        invalid_numbers += percent_per_move
    elif current_number <= 9:
        total_points += 0.2 * current_number
        percent_less_nine += percent_per_move
    elif current_number <= 19:
        total_points += .3 * current_number
        percent_less_nineteen += percent_per_move
    elif current_number <= 29:
        total_points += .4 * current_number
        percent_less_twenty_nine += percent_per_move
    elif current_number <= 39:
        total_points += 50
        percent_less_thirty_nine += percent_per_move
    elif current_number <= 50:
        total_points += 100
        percent_less_than_fifty += percent_per_move
print(f"{total_points:.2f}\nFrom 0 to 9: {percent_less_nine:.2f}%\nFrom 10 to 19: {percent_less_nineteen:.2f}%\nFrom 20 to 29: {percent_less_twenty_nine:.2f}%\nFrom 30 to 39: {percent_less_thirty_nine:.2f}%\nFrom 40 to 50: {percent_less_than_fifty:.2f}%\nInvalid numbers: {invalid_numbers:.2f}%")

