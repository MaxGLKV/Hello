def add(a, b):
    print("ADDING %r + %r" % (a, b))
    return(a + b)
    
def subtract(a, b):
    print("SUBTRACTING %r - %r" % (a, b))
    return(a - b)
    
def multiply(a, b):
    print("MULTIPLYING %r * %r" % (a, b))
    return(a * b)

def divide(a, b):
    print("DIVIDING %r / %r" % (a, b))
    return(a / b)
    
print("I'll try to solve this equation 24 + 34 / 100 - 1023")

x = add(24, subtract(divide(34, 100), 1023))
y = 24 + 34 / 100 - 1023
print(x, y)