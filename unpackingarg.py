def multiply(*args):
    product = 1
    for i in args:
        product *= i 
    return product
    
print(multiply(1,3,4))

def add(x,y):
    return x+y

num = [2,3]
print(add(*num))

def named(**kwargs):
    print(kwargs)
    
def print_nicely(**kwargs):
    named(**kwargs)
    for arg,value in kwargs.items():
        print(f"{arg}: {value}")
        
print_nicely(name="Bob", age=25)

