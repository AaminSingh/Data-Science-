from ast import Lambda


def add(a,b):
  return a+b

def sub(a,b):
  return a-b 

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

result = add(3,4)
#print("the addition value is ",result) 

def cube(num01):
   return num01**3
#num01 = int(input("Enter the number: "))
#print(cube(num01))


#Write a function is_prime(n) that returns True if n is a prime number, otherwise False.  

def is_prime(n):
   if(n==1):
     return False
   elif(n==2):
     return True
   for i in range(2,n):
     if(n%i ==0):
       return False
   return True
print(is_prime(9))


#ARGS  *args allows a function to accept any number of positional arguments.

def demo(*args):
    print(args)

demo(10, 20, 30, 40)


#Kwargs  **kwargs allows a function to accept any number of keyword arguments.
def demo(**kwargs):
    print(kwargs)

demo(name="Aamin", age=22)


#LAMBDS FunctionS  A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
square = lambda x: x**x
print(square(7))










