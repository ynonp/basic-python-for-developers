import re

class Cloth:
    def __init__(self):
        self.matrix = {}

    def mark(self, claim):
        for i in range(claim.x, claim.x + claim.w):
            for j in range(claim.y, claim.y + claim.h):
                if (i, j) not in self.matrix:
                    self.matrix[(i, j)] = []

                self.matrix[(i, j)].append(claim.id)

    def matching(self, criteria):
        return [v for v in self.matrix.values() if criteria.fn(v)]

class Claim:
    def __init__(self, line):
        pattern = "#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)"
        data = re.fullmatch(pattern, line.strip()).groupdict()
        self.id = int(data['id'])
        self.x = int(data['x'])
        self.y = int(data['y'])
        self.w = int(data['w'])
        self.h = int(data['h'])

class Criteria:
    def __init__(self, fn):
        self.fn = fn

cloth = Cloth()

with open('input.txt') as input_file:
  for line in input_file:
    claim = Claim(line)
    cloth.mark(claim)

criteria = Criteria(lambda claims: len(claims) > 1)

# Print how many squares are claimed by more than one elf
print(len(cloth.matching(criteria)))

class OverlappingChecker:
    def __init__(self):
        self.seen_double = set([])
        self.seen_all    = set([])

    def check(self, claims):
        for id in claims:
            if len(claims) > 1:
                self.seen_double.add(id)
            self.seen_all.add(id)

#Print the ID of the only claim that doesn't overlap
c = OverlappingChecker()
criteria = Criteria(c.check)
cloth.matching(criteria)
print(c.seen_all.difference(c.seen_double))

print(cloth.matrix)
print(c.seen_double)
print(c.seen_all)