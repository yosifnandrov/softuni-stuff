from collections import defaultdict


d = defaultdict(int)
word = "hello,madafakas"
for w in word:
    d[w] += 1


print(d)