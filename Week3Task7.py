"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
Bag,hello,without,world
"""

input_str = input('Enter comma separated list of words: ')
words = input_str.split(',')
words.sort()
print(words)