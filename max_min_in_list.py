def find_max(list):
    max=list[0]
    for number in list:
        if number > max:
            max = number
    return max
def find_min(list):
    min=list[0]
    for number in list:
        if number < min:
            min = number
    return min

numbers=[2,48,5,34,25,78,33]

print(f"minimum: {find_min(numbers)}")
print(f"maximum: {find_max(numbers)}")
# ---------------------------------------------------------------
# numbers = [5, 3, 8, 7, 11, 9, 26, 19, 23, 29, 25, 17]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(f"max: {max}")  # formatted text
#
# min = numbers[0]
# for number in numbers:
#     if number < min:
#         min = number
# print('min: ' + str(min))  # min is integer so to concatenate we make it string
