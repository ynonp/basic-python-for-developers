
x = [50, 20, 30, 40]
y = ['a', 'b', 'c']


x.sort()
x.append(100)

print(x[2])
print(x)

######### Using Object Oriented

# students = ClassStudents('students.txt')
#
# print("The the best student is: ", students.highest_grader())
# print("Excellent students: ", students.excellent())


############ Object Oriented Syntax

class Critter:
    def __init__(self):
        self.size = 0

    def eat(self):
        self.size += 1
        print(f"Yummy I already ate {self.size} portions")

    def die(self):
        print("XXX")


c = Critter()
d = Critter()

c.eat()
c.eat()
c.eat()


Critter.eat(d)
d.eat()

print(c.size)


###############################


class Players:
    names = ['bill', 'cliff']

    def add_player(self, name):
        self.names.append(name)


p = Players()
r = Players()

p.add_player('ynon')
print(r.names)















