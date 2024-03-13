def rm_duplicates(list):
    unique = []
    for number in list:
        if number not in unique:
            unique.append(number)
    return unique

numbers=[1,3,3,4,5,5,7,9,78,78,6,5,48,8,8,8,0]
print(rm_duplicates(numbers))

# output:
# [1, 3, 4, 5, 7, 9, 78, 6, 48, 8, 0]

