# this is a module containing 1 function and this is imported in modules.py
def find_max(numbers): # numbers parameter for a list
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum