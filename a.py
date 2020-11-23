my_functions = []

for i in range(4):
    my_functions.append(lambda: print(f"I am function {i}"))

# This all prints the same text
my_functions[0]()
my_functions[1]()
my_functions[2]()
my_functions[3]()

