# Lab:

# Get the program below to print only the
# NAME and IP ADDRESS of each network interface

# Regexp for ANYTHING (including newlines)
# "(\n|.)*"
# "[\n\w\W]*"
# \w - [a-zA-Z0-9_]

import re
pattern = "(?P<name>[-\w]+):[\n\w\W]*inet (?P<ip>[\d.]+)[\n\w\W]*"

interfaces = []
with open('regexp_lab.txt', 'r') as f:
    data = f.read()
    #print(data)
    interfaces = data.split("\n\n")

print(f"There are {len(interfaces)} network interfaces")

for ith in interfaces:
    match = re.fullmatch(pattern, ith)
    if match:
        print(match.groupdict())