import math


def calculator():
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    def square(a):
        return a**2
    def square_root(a):
        return math.sqrt(a)

    print("sum")
    print("subtract")
    print("multiply")
    print("divide")
    print("square")
    print("square_root")
    fvrt = int(input("enter a number(1-6)"))
    if fvrt == 6:
        num=int(input("enter a number"))
        print(square_root(num))
    elif fvrt == 5:
        num=int(input("enter a number"))
        print(square(num))
    elif fvrt in [1,2,3,4]:
        num1=int(input("enter a number"))
        num2=int(input("enter a number"))
    if fvrt == 1:
        print(add(num1,num2))
    elif fvrt == 2:
        print(subtract(num1,num2))
    elif fvrt == 3:
        print(multiply(num1,num2))
    elif fvrt == 4:
        print(divide(num1,num2))

calculator()

