print("-----------------WEEK 2 Task 4-----------------")

class Wee2Task4:
    def __init__(self,sentence):
        self.sentence=sentence

    def inputFromConsole(self):
        self.sentence=input("Enter Sentence: ")

    def printSentence(self):
        print("Sentence is: "+self.sentence)

testObj=Wee2Task4("Constructor")
testObj.inputFromConsole()
testObj.printSentence()