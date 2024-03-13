# python 3 module index --- search it in google

import random

for i in range(3):
    print(random.random())  # between 0 to 1
    print(random.randint(10, 20))

members = ['John', 'Sambit', 'Mosh']
leader = random.choice(members)  # random choice from the elements of members list
print(leader)


class Dice:

    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second       # python automatically interprets this as tuple

dice = Dice()
print(dice.roll())

#-----------

from pathlib import Path  # Path is a class in pathlib module

#Absolute path --> right from the harddisk c:\... and Relative path like from ecommerce directory
# lets use relative path from ecommerce directory
path = Path("ecommerce")
print(path.exists())  # prints 'True'

path = Path("emails")
print(path.exists())  # prints 'False' as no emails directory

path = Path("emails")
print(path.mkdir())  # prints 'None' --> a new directory 'emails' is created

path = Path("emails")
print(path.rmdir())  # prints 'None' --> deletes/removes the directory 'emails'

path = Path()
print(path.glob('*.*'))  # all files in current directories

path = Path()
print(path.glob('*'))  # all files & directories --> everything

path = Path()
print(path.glob('*.py')) # all py files in the current directory

path = Path()
print(path.glob('*.xls'))

# <generator object Path.glob at 0x0000015305A2CAE0>
# <generator object Path.glob at 0x0000015305A2CAE0>
# <generator object Path.glob at 0x0000015305A2CAE0>

path = Path()
for file in path.glob('*.py'):  # all py files in the current directory
    print(file)

# output:
# 1.py
# built_in_modules.py
# cargame.py
# classes.py
# converters.py
# coordinate.py
# dict_example.py
# emoji_converter.py
# exceptions.py
# functions.py
# guessgame.py
# inheritance.py
# largest_in_list.py
# max_min_in_list.py
# modules.py
# names.py
# rm_duplicate.py
# shopping_cart.py
# unpacking.py
# utils.py
# weight.py

path = Path()
for file in path.glob('*'):  # all files & directory
    print(file)

# output:
# .git
# .idea
# .venv
# 1.py
# built_in_modules.py
# cargame.py
# classes.py
# converters.py
# coordinate.py
# dict_example.py
# ecommerce
# emoji_converter.py
# exceptions.py
# functions.py
# guessgame.py
# inheritance.py
# largest_in_list.py
# max_min_in_list.py
# modules.py
# names.py
# qodana.yaml
# rm_duplicate.py
# shopping_cart.py
# unpacking.py
# utils.py
# weight.py
# __pycache__

