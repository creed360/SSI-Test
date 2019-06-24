"""This module contains all the required decorators"""

import timeit

#Decorator for Task 13
def find_time(function):

    #This is the inner function.
    #It can access the function
    #passed as argument
    def find_time_wrapper():
        print(timeit.timeit(function))

    return find_time_wrapper

#Decorator for Task 14
def make_singleton(clas):

    class_instances = {}
    def make_singleton_wrapper():
        if clas not in class_instances:
            class_instances[clas] = clas()
        return class_instances[clas]
    return make_singleton_wrapper