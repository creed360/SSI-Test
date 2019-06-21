"""Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.

Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
print("-----------------WEEK 2 Task 4-----------------")

class Wee2Task4:
    def __init__(self,sentence):
        self.sentence=sentence

    def inputFromConsole(self):
        self.sentence=input("Enter Sentence: ")

    def printSentence(self):
        print("Sentence is: "+self.sentence)

testObj = Wee2Task4("Constructor")
testObj.inputFromConsole()
testObj.printSentence()