"""Write a Python program to remove the parenthesis area in a string.

Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

Expected Output:
example
w3resource
github
Stackoverflow

Hint: Use Regular expressions
"""
import re
examples = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
examples = ["example (.com) is just an example", "w3resource", "github (.com) is to keep repositories", "stackoverflow (.com) knows everything"]
for example in examples:
    print(re.sub(" ([(].com[)])","",example))
