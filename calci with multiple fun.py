
def addition(a,b):
    return a+b
def multiply(a,b):
    return a*b
def calculate(f,a,b):
    return f(a,b)
add = calculate(addition,2,3)
product = calculate(multiply,4,5)
print("Addition:", add)
print("Multiplication:", product)
