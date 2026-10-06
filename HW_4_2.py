numbers = [0, 1, 7, 2, 4, 8]

if len(numbers) == 0:
    print(0)
else:
    sum_numbers = 0

    for i in range(0, len(numbers), 2):
        sum_numbers += numbers[i]

    result = sum_numbers * numbers[-1]

    print(result)