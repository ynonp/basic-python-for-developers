import re

pattern = "(?P<min_count>\d+)-(?P<max_count>\d+) (?P<char>\w): (?P<text>\w+)"
text = "1-3 a: abcde"

match = re.fullmatch(pattern, text)
if match is not None:
    data = match.groupdict()
    print(data)
    print(f"min_count = {data['min_count']}; max_count = {data['max_count']}")


if match := re.fullmatch(pattern, text):
    data = match.groupdict()
    print(data)
    print(f"min_count = {data['min_count']}; max_count = {data['max_count']}")






