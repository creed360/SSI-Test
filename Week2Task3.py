print("\n-----------------WEEK 2 Task 3-----------------")

squares={}
try:
    integral=int(input("Enter Integral: "))
    for i in range(1,integral+1):
        squares[i]=i*i
    print(squares)
except ValueError:
    print("Wrong Input!")