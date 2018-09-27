#define a fx
def example(a,b):
    print('basic function')
    z = a+b
    print(z)

#call it
example(45,2)

def multi(a,b):
    print('  a multiplication function')
    z = a * b
    print(z)

multi(5,3)

#default parameters
def gon(size,age=11):
    t=size * age
    print(t)

gon(47)



#global and local vars
x=6
#this can be used but its not a global variable because u cant do operations on it
def example():
    print(x)


example()


#global variable
y=6

def examp():
    global y #we defined it like this
    print(y)
examp()

#in case u cant use global variables
z=5
def ex():
    globz=z
    globz=globz+4
    print(globz)
    return globz
val=ex()

print(val)