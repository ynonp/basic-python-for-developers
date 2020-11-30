# Working with Files


# Open file as binary
open('words.txt', 'rb')


## File Encoding
f1 = open('words.txt', 'r', encoding='utf8')
try:
    print(int('hahaha'))
except ValueError:
    pass
finally:
    f1.close()


## with
with open('words.txt', 'r', encoding='utf8') as file:
    print(file.readline())
    # return 10
    #print(int('hahaha'))

# Now file is closed


## File read/write patterns

### Copy file
with open('words.txt', 'r', encoding='utf8') as fin, \
    open('words2.txt', 'w', encoding='utf16') as fout:
    for line in fin:
        fout.write(line)

# Change File In Place
import fileinput

with fileinput.input("demo.txt", inplace=True) as file:
    for line in file:
        # line already has a \n
        # "one\n|"
        if not line.startswith('#'):
            print(line, end="|")


## Lab

