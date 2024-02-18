import math
a = math.sqrt(36)
b = math.ceil(1.4)
c = math.floor(1.4)
d = math.pi
print(a)
print(b)
print(c)
print(d)
import datetime
dt = datetime.datetime.now()
print(dt)
print(dt.year)
print(dt.strftime("%A"))
#declaring a function
def fun():
    print("BANOQABIL")
    print("Name:Muhammad Abdul Baseer")
    print("Father Name: Muhammad Ayub")
    print ("Bazm e sathi")
    #driver's code
    #calling function 
fun()
def evenOdd ( x ):
    if (x%2==0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)
#python program to demonstrate
#default arguments
def myFun(x, y=50):
    print("x:", x)
    print("y:", y)
    #Driver's code
myFun(10)
def student(firstname,lastname):
    print(lastname,firstname)
#keyword arguments
student(firstname='geeks',lastname='practice')
student(lastname ='practice',firstname='geeks')
#function with two arguments
def add_numbers(num1,num2):
    sum = num1 + num2
    print("sum:",sum)
#function call with two values
add_numbers(5,4)
