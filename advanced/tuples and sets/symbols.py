from collections import defaultdict
my_dict = defaultdict(int)
text = input()
for symbol in text:
    my_dict[symbol] = text.count(symbol)


my_dict = dict(sorted(my_dict.items(), key = lambda x:x[0]))
for symbol, count in my_dict.items():
    print(f"{symbol}: {count} time/s")


