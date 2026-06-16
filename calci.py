import math
def calculator():
    def addition(a,b):
        return a+b
    def subtraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b
    def square(a):
        return a**2
    fvrt = int(input())
    if fvrt == 5:
        num=int(input())
        print("Result:", square(num))
    elif fvrt in [1,2,3,4]:
        num1=int(input())
        num2=int(input())
    if fvrt == 1:
        print("Result:", addition(num1,num2))
    elif fvrt == 2:
        print("Result:", subtraction(num1,num2))
    elif fvrt == 3:
        print("Result:", multiplication(num1,num2))
    elif fvrt == 4:
        print("Result:", division(num1,num2))

calculator()

