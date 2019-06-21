"""Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9

Then, the output should be:
1,3,5,7,9
"""

numbers = input('Enter comma separated list of numbers: ')
numbers = numbers.split(',')
odd_numbers = []
for number in numbers:
    try:
        number=int(number)
        if number % 2 != 0:
            odd_numbers.append(number ** 2)

    except ValueError:
        print("List must contain numbers only!")
        exit()

print(odd_numbers)