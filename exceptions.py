# age = int(input('Age: '))
# print(age)

# Age: 21
# 21
#
# Process finished with exit code 0

# Age: hi
# Traceback (most recent call last):
#   File "C:\Users\KIIT\PycharmProjects\first\exceptions.py", line 1, in <module>
#     age = int(input('Age: '))
#           ^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'hi'


# process finished with exit code 0 --> means our program terminated successfully
# anything but 0 means crashed like 1

# ----------------------------------------
# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError:
#     print('Invalid Value')  # if error type is valueError then print invalid value
#----------------------------
# Age: 21
# 21
#
# Process finished with exit code 0

# Age: hi
# Invalid Value
#
# Process finished with exit code 0
#
#--------------------
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)
# except ZeroDivisionError:
#     print('Age cannot be 0.')
# except ValueError:
#     print('Invalid Value.')
#----------------------------------------
# Age: 0
# Age cannot be 0.
#
# Process finished with exit code 0
# ----------------------------

# Exception handling in Python

try:
    # Code that might raise an exception
    num_str = input("Enter an integer: ")
    num = int(num_str)

    result = 10 / num

except ValueError:
    # Handle the case when the user enters a non-integer
    print("Invalid input. Please enter an integer.")

except ZeroDivisionError:
    # Handle the case when the user enters 0
    print("Cannot divide by zero. Please enter a non-zero number.")

else:
    # Code to be executed if no exception is raised
    print("Result:", result)

finally:
    # Code to be executed whether an exception is raised or not
    print("Finally block: This will always execute.")
