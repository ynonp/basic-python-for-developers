# def defines a function
def f(x, y):
    return x + y


f(10, 20)
f(x=10, y=20)
f(y=30, x=10)

####################################

# Default parameter values
def print_times(text, times=5):
    for i in range(times):
        print(text)



print_times("hello")
print_times("bye bye", times=2)
print_times("wow", 5)


#######################################

# Variadic Functions
def sum_squares(*numbers):
    res = 0
    for i in numbers:
        res += i * i

    return res


sum_squares(10, 20, 30, 50, 11)


####################################

y = lambda x: x * x
twice = lambda x, y: x * y * 2

print(y(4))
print(twice(5, 2))



################################

functions = []
for i in range(4):
    functions.append(lambda: print(i))

functions[0]()
functions[1]()
functions[2]()
functions[3]()








