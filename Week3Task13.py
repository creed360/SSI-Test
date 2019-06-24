"""Write a decorator @timee. It will measure the time a function takes to execute and print the duration to the console.

Try this decorator on 3 different functions to check the execution time of each function
"""
import timeit

#Defining Decorator
def find_time(function):

    #This is the inner function.
    #It can access the function
    #passed as argument
    def find_time_wrapper():
        print(timeit.timeit(function))

    return find_time_wrapper

@find_time
def test_func1():
    return 10 ** 10

@find_time
def test_func2():
    return 110 ** 11

@find_time
def test_func3():
    return 220 ** 12

test_func1()
test_func2()
test_func3()