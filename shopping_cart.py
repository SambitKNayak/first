# # prices = [10, 20, 30]
# # total = 0
# # for price in prices:
# #     total += price
# # print(f"Total: {total}")
#
print("""
WELCOME TO SKN MART

Product List

pno   item       price
1  -  chocolate - 100/-
2  -  rice      - 50/-
3  -  dal       - 70/-
4  -  sugar     - 55/-
5  -  salt      - 51/-
6  -  apple     - 200/-
7  -  orange    - 130/-
8  -  milk      - 25/-
9  -  potatoes  - 33/-
10 -  tomatoes  - 59/-
11 -  quit ------------------------
""")

item_price = {1: 100, 2: 50, 3: 70, 4: 55, 5: 51, 6: 200, 7: 130, 8: 25, 9: 33, 10: 59}
total = 0
while True:
    command = int(input("enter the pno of items you wanna buy : "))
    # command = f'{command1}'
    # command = str(command1)
    for key in item_price:
        if key == command:
            total += item_price[key]
            print(f"Your current total is : {total}")
    if command == 11:
        print(f"Total: {total}")
        print("Thank you for shopping with us!")
        break

# ----------------------------------------------------------------------
# command = int(input("enter the pno of items you wanna buy : "))  # 5
# command1 = f'{command}'  # 5
# command2 = str(command)  # 5
