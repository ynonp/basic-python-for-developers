
shapes = {
    'triangle': 3,
    'rectangle': 4,
    'line': 1,
}

print(shapes['line'])
shapes['star'] = 5

for key, value in shapes.items():
    print(f"{key} => {value}")

