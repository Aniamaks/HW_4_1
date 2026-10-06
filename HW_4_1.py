numbers = [0, 1, 0, 12, 3]

for i in range(numbers.count(0)):
    numbers.remove(0)
    numbers.append(0)

print(numbers)