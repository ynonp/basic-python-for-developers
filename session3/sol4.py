from typing import List


def sum_2_numbers(num1: int, num2: int):
    return num1 + num2


def bigger_than(treshold: int, values: List[int]):
    # [2, 5, 8, 40, 50, 60, 70] -> [40, 50, 60, 70]
    # List Comprehension general rule
    # [f(x) for x in list if p(x)]
    return [x for x in values if x > treshold]

print(sum_2_numbers(10, 20))
print(sum_2_numbers("hello", "world"))
print(bigger_than(10, [2, 5, 8, 40, 50, 60, 70]))




# Solution 3
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


print(sorted(data, key=lambda item: item.name))
print(sorted(data, reverse=True, key=lambda x: (x.grade, x.name)))










