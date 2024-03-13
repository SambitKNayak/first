secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print("Sorry! You failed!")

# Alternate

# import random
#
# secret_number = random.randint(1, 100)
# # guessed_number = int(input("Guess the number: ")) ---> this will be extra so no need
# guess_count = 0
#
# while True:
#     guessed_number = int(input("Guess the number: "))
#     guess_count += 1
#     if guessed_number == secret_number:
#         print("you guessed it right! and in " + str(guess_count) + " attempts!")
#         break
#     elif guessed_number < secret_number:
#         print("secret number is higher")
#     else:
#         print("secret number is lower")
# else:
#     print("Sorry! You failed!")