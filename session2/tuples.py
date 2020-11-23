import collections

Student = collections.namedtuple('Student', ['name', 'grade'])


point = (10, 10, 'red')
top_left = (10, 10)
bottom_right = (90, 90)
center = (50, 50)

jimmy = Student(name='jimmy', grade=92)
jane  = Student(name='jane', grade=92)


print(jimmy.grade)
print(len(point))
print(point[0])
print(point[1])
print(point[-1])

print(jimmy)