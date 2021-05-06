tickets_to_check = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]
is_jackpot = False
def is_it_jackpot(list_right,list_left,list):
    for single_symbol in list_right:
        if single_symbol in winning_symbols:
            if list_right == 10*single_symbol:
                if list_left == list_right:
                    print(f'ticket "{list}" - 10{single_symbol} Jackpot!')
                    return True


def is_it_winning(list_right,list_left,list):
    for symbol in winning_symbols:
        if 6*symbol in list_right:
            if 6 * symbol in list_left:
                symbols_in_left = list_left.count(symbol)
                symbols_in_right = list_right.count(symbol)
                return print(f'ticket "{list}" - {min(symbols_in_right,symbols_in_left)}{symbol}')
            else:
                return print(f'ticket "{single_ticket}" - no match')
    return print(f'ticket "{single_ticket}" - no match')

for single_ticket in tickets_to_check:
    single_ticket = single_ticket.strip()
    if not len(single_ticket) == 20:
        print("invalid ticket")
    else:
        left_side = single_ticket[:len(single_ticket)//2]
        right_side = single_ticket[len(single_ticket)//2:]
        if not is_it_jackpot(left_side,right_side,single_ticket):
            is_it_winning(left_side,right_side,single_ticket)










