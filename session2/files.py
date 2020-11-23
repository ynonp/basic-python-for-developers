
# Read from a text file
with open('inputs/input1.txt', 'r', encoding='utf8') as fin:
    for index, line in enumerate(fin):
        print(line, end='')


# Write to a text file
with open('mynewfile.txt', 'w', encoding='utf8') as fout:
    for i in range(10):
        fout.write(f"Welcome home {i}\n")
