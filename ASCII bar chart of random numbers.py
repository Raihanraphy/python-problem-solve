import random

data = [random.randint(1, 20) for _ in range(10)]

for i, num in enumerate(data, 1):
    bar = '#' * num
    print(f"{i:2}: {bar} ({num})")
