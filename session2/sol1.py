seen = set()

with open('inputs/input1.txt', 'r', encoding='utf8') as fin,\
     open('inputs/output1.txt', 'w', encoding='utf8') as fout:
    for line in fin:
        if line[0] not in seen:
            seen.add(line[0])
            fout.write(line)

