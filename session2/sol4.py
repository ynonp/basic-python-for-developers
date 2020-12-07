from typing import List

## 1
def add_two_numbers(a: int, b: int) -> int:
    return a + b

add_two_numbers(2, 5)

## 2
def higher_than(val: int, data: List[int]) -> List[int]:
    return [v for v in data if v > val]

higher_than(10, [5, 8, 9, 22, 15, 9])


## 3
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade'])

data = [
  Student('john', 80),
  Student('bill', 70),
  Student('anna', 95),
  Student('brandon', 90),
  Student('zoe', 89),
  Student('tim', 9)
]

sorted(data, key=lambda s: s.name)
sorted(data, key=lambda s: s.grade)[::-1]

## 4

my_functions = []

for i in range(4):
    my_functions.append(lambda: print(f"I am function {i}"))

# This all prints the same text
my_functions[0]()
my_functions[1]()
my_functions[2]()
my_functions[3]()

