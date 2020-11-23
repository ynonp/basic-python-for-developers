from typing import List, Tuple
import random

def save_line(words: List[Tuple[str, str]], line: str):
    # line = "boy / garçon"
    left, _, right = line.strip().partition(' / ')
    words.append((left, right))


words: List[Tuple[str, str]] = []
with open('inputs/translation.txt') as fin:
    for line in fin:
        save_line(words, line)


#print(words)

while True:
    left, right = random.choice(words)
    if random.randint(0, 1) == 0:
        left, right = right, left

    print(left)
    if input() == right:
        print("Bravo!")





