weight = int(input("Weight: "))
unit = input('unit is in (L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = round(weight * 0.45)   #converted = (weight * 0.45)
    print(f"You are {converted} kilos")
else:
    converted = round(weight / 0.45)
    print(f"You are {converted} pounds")
