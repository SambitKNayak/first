# def greet_user():
#     print('Hi there!')
#     print('Welcome Aboard.')
#
# print("Start")
# greet_user()
# print("Finish")

# def greet_user(first_name, last_name):     # name --> parameter thats placeholder defined in this function that receive info
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome Aboard.')
#
# print("Start")
# # positional arguments: order/position matters
# greet_user("Sambit", "Nayak")  # "Sambit" --> argument thats actual info we supply to this function
# # keyword arguments: position doesn't matter --> better readability
# greet_user(last_name="Nayak",first_name="Sambit")
# greet_user("Sambit", last_name="Nayak")
# # greet_user(first_name="Sambit", "Nayak")  # error
# print("Finish")

# def square(number):
#     return number * number
# result = square(3)
# print(result)
#
# print(square(4))
# print(square(5))
# print(square(7))
# print(square(9))
# print(square(89))

# def square(number):
#     print(number * number)
# square(3)
# 9

# def square(number):
#     print(number * number)
# print(square(3))
# 9
# None  --> by default a function returns None
#
# our 'function' shouldn't worry about getting 'input' and giving 'output' so using return is better

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",  # windows logo + . ---> shortcut for emojis
        ":(": "😞",
        ":x": "😡",
        ":!": "😱",
        ":[": "😩",
        ":+": "😵"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " " # if there is no value for inserted key 'word' then return the same inserted 'word' that set as default value in get function
    return output

message = input(">")
print(emoji_converter(message))

# >i am happy :)
# i am happy 😊