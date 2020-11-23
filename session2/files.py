
# Read from a text file
with open('lab3.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        print(line, end='')


# Write to a text file
with open('mynewfile.txt', 'w', encoding='utf8') as fout:
    for i in range(10):
        fout.write(f"Welcome home {i}\n")
