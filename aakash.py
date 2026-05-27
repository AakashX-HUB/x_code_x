#FUNCTION
#1

def add():
    a=13
    b=12
    print("add")
add()
#2
def sub():
    a=12
    b=13
    print("sub:")
sub()    
#3
a=int(input("enter a"))
b=int(input("enter b"))
def add(a,b):
    print(a+b)
add(a,b)
#4
def details(name="jaa",course="java",clg="AIML"):
    print(name)
details()
#5
def fun(**a):
    for i,j in a.items():
        print(i,j)
fun(name="abc",age=2,city="salem")
#6
def demo(*p):
    for i in p:
        print(i)
demo()
def fun(**a):
    for i,j in a.items():
        print(i,j)
    fun(name="abc",age=2,city="salem")
def demo(*a):
    for i in a:
        print(i*2)
demo(1,2,3,4,5,6,6)        
#7 lambda
g=lambda a,b:a*b
print(g(1,2))
g1=(lambda a,b:a+b)
print(g1(1,2))
#8 return
def demo():
    for i in range(1,10):
        return(i)
print(demo())
#9recurtion
def fib(num):
    if num==0 or num==1:
        return num
    elif num>=1:
        return fib(num-2)+fib(num-1)
print(fib(7))
#9


    
