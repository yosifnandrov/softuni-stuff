import re


dates = input()
pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

date = re.finditer(pattern,dates)

for d in date:
    dict = d.groupdict()
    print(f'Day: {dict["day"]}, Month: {dict["month"]}, Year: {dict["year"]}')