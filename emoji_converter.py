# message = input(">")
# words = message.split(' ')
# print(words)

# >im sambit how you doing
# ['im', 'sambit', 'how', 'you', 'doing']

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",   # windows logo + . ---> shortcut for emojis
#     ":(": "😞",
#     ":x": "😡",
#     ":!": "😱",
#     ":[": "😩",
#     ":+": "😵"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# >i am happy :)
# i am happy 😊

# >i am sad :(
# i am sad 😞

# >i am shocked :!
# i am shocked 😱

# # ----------------------------------------
#  only emoji as output
# def emoji_converter(message):
#     emojis = {
#         ":)": "😊",  # windows logo + . ---> shortcut for emojis
#         ":(": "😞",
#         ":x": "😡",
#         ":!": "😱",
#         ":[": "😩",
#         ":+": "😵"
#     }
#     return emojis.get(message, message)
#
# message = input(">")
# print(emoji_converter(message))
# ----------------------------------------------------

# emoji with some text
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
        output += emojis.get(word, word) + " " # if there is no value for inserted key 'word' then return the same inserted 'word' thats set as default value in get function
    return output

message = input(">")
print(emoji_converter(message))

# >i am happy :)
# i am happy 😊

# >i am angry :x
# i am angry 😡

# >:) :(
# 😊 😞