import itertools
import re


key = input().split()
hidden_message = input()
result = ""
normal_msgs = []

while not hidden_message == "find":
    combined = zip(hidden_message, itertools.cycle(key))
    for char, num in combined:
        result += chr(ord(char) - int(num))
    normal_msgs.append(result)
    result = ""
    hidden_message = input()

for msg in key:
    treasure_type = re.search(re.escape('&')+'(.*)'+re.escape('&'), msg).group(1)
