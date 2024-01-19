numbers = [5, 3, 8, 7, 11, 9, 26, 19, 23, 29, 25, 17]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"max: {max}")  # formatted text

min = numbers[0]
for number in numbers:
    if number < min:
        min = number
print('min: ' + str(min))  # min is integer so to concatenate we make it string
