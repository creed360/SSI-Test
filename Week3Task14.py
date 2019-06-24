"""Write a decorator which convert each class to Singleton class.
(A singleton is a class with only one instance)
"""

class abc:

    def __init__(self):
        print("Constructor")

    def foo(self):
        print("Class ABC")

def singleton_decorator(clas):

    class_instances = {}
    def inner():
        if clas not in class_instances:
            class_instances[clas] = clas()
        return class_instances[clas]
    return inner

my_class=singleton_decorator(abc)

object = my_class()

#This time constructor will not be called
object2 = my_class()

