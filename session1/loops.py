x: int = 99

while x > 0:
    text: str = f"{x} bottles of beer on the wall"
    print(text)
    x -= 1


print("No more bottles of beer on the wall")

###############################
for index, fruit in enumerate(['Banana', 'Apple', 'Orange']):
    print(f"fruit {index} is {fruit}", end=" <-> ")

for number in range(2, 10, 3):
    print(number)

for letter in "hello":
    print(letter)







