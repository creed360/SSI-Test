print("-----------------WEEK 2 Task 2-----------------")
numbers=[]
for i in range(1000,2001):
    if i%7 == 0 and i%5 != 0:
        numbers.append(i)
print("Numbers that are divisible by 7 and not a multiple of 5 are in range 1000 and 2000 inclusive are: ")
print(numbers)