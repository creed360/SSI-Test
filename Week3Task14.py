"""Write a decorator which convert each class to Singleton class.
(A singleton is a class with only one instance)
"""

def make_singleton(clas):

    class_instances = {}
    def make_singleton_wrapper():
        if clas not in class_instances:
            class_instances[clas] = clas()
        return class_instances[clas]
    return make_singleton_wrapper

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