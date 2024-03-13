phone = input("Phone: ")
numbers = {"1" : 'One ', "2" : 'Two ', "3" : 'Three ', "4" : 'Four ', "5" : 'Five ' }
output = ""
for ch in phone:
    output += numbers.get(ch, "!")
print(output)

