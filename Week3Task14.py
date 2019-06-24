"""Write a decorator which convert each class to Singleton class.
(A singleton is a class with only one instance)
"""
from decorators import make_singleton

@make_singleton
class Person:

    def __init__(self):
        print("Person Constructor")

    def speak(self):
        print("Person Speaks")

ali = Person()
ali.speak()

#This time constructor will not be called again
ahmad = Person()
