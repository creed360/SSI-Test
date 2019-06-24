"""Write a decorator @timee. It will measure the time a function takes to execute and print the duration to the console.

Try this decorator on 3 different functions to check the execution time of each function
"""
from decorators import find_time

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