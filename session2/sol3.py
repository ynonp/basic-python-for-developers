"#1279 @ 533,425: 14x25"
from typing import Dict, Tuple, List

# List Comprehension
numbers = [10, 20, 30, 40, 5, 7, 9]
squares = [n * n for n in numbers]
even    = [n for n in numbers if n % 2 == 0]
odd     = [(n * n) for n in numbers if n % 2 == 1]

# General rule:
# [f(x) for x in seq if p(x)]

x, y = [int(t) for t in '10,18'.split(',')]



def save_line(claims: Dict[Tuple[int,int], List[str]], line: str):
    id = line.split('@')[0].strip()
    x, y = [int(t) for t in line.split('@')[1].split(':')[0].strip().split(',')]
    w, h = [int(t) for t in line.split('@')[1].split(':')[1].strip().split('x')]

    for i in range(x, x + w):
        for j in range(y, y + h):
            if (i, j) not in claims:
                claims[(i, j)] = []

            claims[(i, j)].append(id)


claims = {}
with open('inputs/input3.txt', 'r', encoding='utf8') as file:
    for line in file:
        save_line(claims, line)


count = len([v for v in claims.values() if len(v) > 1])
print(count)
