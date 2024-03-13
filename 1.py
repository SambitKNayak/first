print("*" * 10)
#
# name = input("what's your name? ")
# age = int(input("what's your age? "))
# color = input("what's your fav color? ")
# print(name + " is " + str(age) + " and likes " + color)
#
course = 'python is a "great language" and i"m learning it'
print(course)
# print(course[0])  # start  --> p
# print(course[-1])  # from last --> t
# print(course[0:3])  # from index 0 to 2 i.e., pyt here
# another = course[:]  # another is same as course here
# print(another)
# course_1 = '''
# Hi Khitish,
#
# Here is our first email to you.
#
# Thank You,
# The support team.
# '''
# print(course_1)
# output:
# Hi Khitish,
#
# Here is our first email to you.
#
# Thank You,
# The support team.
#----------------------------------------------------
# name = 'sambit'
# print(name[1:-1])
#
# first = "Sambit"
# middle = "Kumar"
# last = "Nayak"
# msg = f'{first} [{middle}] {last} is a coder'
# print(msg)
#
course = 'Python is Great'
print(len(course))     # 15
print(course.upper())  # PYTHON IS GREAT
print(course.lower())  # python is great
course.upper()         # doesn't convert course to upper case permanently
print(course)          # Python is Great
print(course.find('P')) # index --> 0
print(course.find('o')) # index --> 4
print(course.find('Great'))  # 10
print(course.replace('Great','Brilliant'))  # Python is Brilliant
print(course.replace('great','Brilliant'))  # Python is Great --> case sensitive so doesn't replace
print(course.replace('P','J'))  # ython is Great
print(course)  # Python is Great --> REPLACE DOESN'T CHANGE STRING PERMANENTLY
print('Python' in course) # True --> boolean
print('python' in course) # False --> boolean
#
# len()
# course.upper()
# course.lower()
# course.title()
# course.find()
# course.replace()
# '...' in course
#
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)  # 3.33
# print(10 // 3)  # 3
# print(10 % 3)  # 1
# print(10 ** 3)  # 1000
#
# # assignment operator '='
# x = 10
# x = x + 3
# x += 3  # augmented or enhanced assignment
# print(x)
# y = 20
# y *= 3
# print(y)
#
# precedence order:
# parenthesis
# exponentiation 2**3
# multiplication or division
# addition or subtraction
# x = (10 + 3) * 2 ** 2
# print(x)
# y = (2 + 3) * 10 - 3
# print(y)
#
x = 2.9
print(round(x))   # 3
print(round(2.5))  # 2
print(round(0.01))  # 0
print(round(0.998))  # 1
print(abs(-3.3))  # 3.3

import math
print(math.ceil(2.9))   # 3
print(math.floor(2.9))  # 2
# refer to python 3 math module documentation for more
#
# is_hot = False
# is_cold = True
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")
#
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f'Down Payment : ${down_payment}')
#
# has_high_income = False
# has_good_credit = True
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# if has_high_income or has_good_credit:
#     print("Eligible for loan")
#
# has_good_credit = True
# has_criminal_record = False
# if has_good_credit and not has_criminal_record:
#     print("Eligible for loan")
#
# temperature = 35
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")
#
# equality  ==
# greater than  >
# >=
# less than  <
# <=
#
# name = input("enter your name: ")
# name_len = len(name)
# if name_len < 3:
#     print("name must be atleast 3 characters long")
# elif name_len > 50:
#     print("name can be a maximum of 50 characters long" )
# else:
#     print("name looks good! ")
#
# print(input("enter the weight: "))
#
# i = 1
# while i <= 5:
#     print('*' * i)
#     i = i + 1
# output:
# *
# **
# ***
# ****
# *****
# print("Done")
#
# import random
# # Generate a random integer between a specified range
# random_number = random.randint(1, 100)
# print("Random number:", random_number)
# # Generate a random floating-point number between a specified range
# random_float = random.uniform(0.0, 1.0)
# print("Random float:", random_float)
#
# for item in 'Python':
#     print(item)
# for item in ['Sambit', 'Mosh']:
#     print(item)
# for item in [1, 2, 3, 4]:
#     print(item)          # 1 2 3 4 in separate lines
# for item in range(10):
#     print(item)          # 0 to 9
# for item in range(5, 10):
#     print(item)          # 5 to 9
# for item in range(5, 10, 2):
#     print(item)          # 5 7 9
#
# a = 'abcdefgh'
# print(a[:-3])  # abcde
# print(a[-3:])  # fgh
# print(a[2:-1])  # cdefg
#
# names = ['John', 'Bob', 'Sambit', 'Mosh', 'Khitish']
# print(names[0])
# print(names[2])
# print(names[-1])
# print(names[-2])
# print(names[2:])
# print(names[2:4])
# print(names[:])
# print(names[-1:])
# print(names[2:-1])
# print(names[:-1])
# print(names)
#
# names[0] = 'Jon'   # rename 'John'
# print(names)

# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix)
# print(matrix[0])
# print(matrix[0][1])
# matrix[0][1] = 20
# print(matrix[0][1])
#
# for row in matrix:
#     for item in row:
#         print(item)
#
# numbers = [5, 2, 1, 5, 7, 4]           # print(numbers.sort()) --> None
# print(50 in numbers)         # False
# print(numbers.count(5))      # 2
# numbers.sort()
# print(numbers)               # [1, 2, 4, 5, 5, 7]
# numbers.reverse()
# print(numbers)               # [7, 5, 5, 4, 2, 1]
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)              # [7, 5, 5, 4, 2, 1]
# numbers.append(20)
# print(numbers)               # [7, 5, 5, 4, 2, 1, 10, 20]
# numbers.insert(0, 10)
# print(numbers)               # [10, 7, 5, 5, 4, 2, 1, 10, 20]
# print(numbers.index(5))      # 2
# numbers.remove(5)
# print(numbers)               # [10, 7, 5, 4, 2, 1, 10, 20]
# numbers.pop()
# print(numbers)               # [10, 7, 5, 4, 2, 1, 10]
# numbers.clear()
# print(numbers)               # []

# [] -- lists
# () -- tuples cannot change or mutate
#
# numbers = (1, 2, 3, 2, 2, 2, 5)
# print(numbers.count(2))   # 4
# print(numbers.index(5))   # 6
#
# {} -- dictionary
customer = {
    "name": "Sambit Nayak",
    "age": 21,
    "is_verified": True
}
print(customer)
print(customer["name"])     # Sambit Nayak
customer["birthdate"] = "Jan 2 2003"
print(customer)
# # print(customer["Name"])   # error as its name not Name
# print(customer.get("Name")) # None
# print(customer.get("name")) # Sambit Nayak
# print(customer["age"])      # 21
# print(customer.get("birthdate", "Jan 2 2003"))  # Jan 2 2003
# customer["name"] = "Sambit Kumar Nayak"
# print(customer)   # {'name': 'Sambit Kumar Nayak', 'age': 21, 'is_verified': True}
# print(customer["name"])  # Sambit Kumar Nayak

# best - use comments to explain 'why' and 'how' not 'what'

# my_string = "Hello, World"
# substring = my_string[-1:-2]   # ""
# substring1 = my_string[-1:]     # d
# print(substring)
# print(substring1)
# ---------------------------------------------------------------------------------------------------














