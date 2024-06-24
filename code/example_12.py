# Logic: Loop on an list

my_lucky_numbers = [7, 13, 17, 23, 31]

for number in my_lucky_numbers:
    print(number)


squared_numbers = []

for number in my_lucky_numbers:
    squared_numbers.append(number**2)

for number in squared_numbers:
    print(number)
