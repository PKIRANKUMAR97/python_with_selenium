# positional arguments
"""
def sub(x, y):
    return x - y


z = sub(8, 4)  # here 8 will go into x position any 4 will go into y position
print(z)
"""
# Required arguments
"""
def sub(x, y):
    return x - y


z = sub()  # here if we dont give arguments , then we will get TypeError  because x,y are required arguments 
print(z)
"""

# optional arguments
"""
def sub(x=90, y=20):
    return x - y


z = sub()  # here if we don't give arguments , then they will take from the function definition i.e 90,20
z1 = sub(10) # here 10 goes to x
z2 = sub(100,107) # x takes 100 value , y takes 107 value
print(z)
print(z1)
print(z2)
"""

#keyword arguments
def sub(x=5, y=4):
    return x - y


z = sub(y=8)  # here 8 will go and replace y position
print(z)