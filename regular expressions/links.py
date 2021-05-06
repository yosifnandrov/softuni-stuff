import re


data = input()

pattern = r"((?<=^)|(?<=\s))w{3}(\.[a-z0-9-]+)+\.[a-z]+((?=\s)|(?=$)|(?=[\!\?\.]))"
websites = []
while data:
    result = re.finditer(pattern,data,re.MULTILINE)
    for res in result:
        websites.append(res.group())
    data = input()

for site in websites:
    print(site)