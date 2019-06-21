"""Write a Python program to find urls in a string and output all urls as list.

Sample data :

My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles
in the portal of http://www.geeksforgeeks.org

Expected Output: [https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles, http://www.geeksforgeeks.org]

Hint: Use Regular expressions
"""

import re

example="My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org"
print(re.findall("http[s]*://[^[/]*",example))
