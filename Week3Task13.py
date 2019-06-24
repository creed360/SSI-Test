"""Write a decorator @timee. It will measure the time a function takes to execute and print the duration to the console.

Try this decorator on 3 different functions to check the execution time of each function
"""
import timeit

def test_func1():
    return 10 ** 10

def test_func2():
    return 110 ** 11

def test_func3():
    return 220 ** 12

#Defining Decorator
def timee_decorator(func):

    #This is the inner function.
    #It can access the function
    #passed as argument
    def inner_func():
        print(timeit.timeit(func))

    return inner_func

timee1=timee_decorator(test_func1)
timee2=timee_decorator(test_func2)
timee3=timee_decorator(test_func3)

timee1()
timee2()
timee3()