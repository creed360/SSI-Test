sentence=input("Enter Sentence: ")

digits=0
letters=0
for i in sentence:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1

print("LETTERS:",letters)
print("DIGITS:",digits)