#num = int("ram")#Value Error
#print(10/0)#NameError ----x not defined
#print(x)
#Type of Built in Error in Python



IndentationError
NameError
TypeError
ValueError
ZeroDivisionError

try:
    numerator = float(input("Enter first value"))
    denominator = float(input("Enter second number"))

    result = numerator/denominator
    print(f"Result:{result}")

except ZeroDivisionError:
    print("Error: you cannot divide by zero")
except ValueError:
    print("Error: Please enter valid number only") 
finally:
    print("the execution done sucessfully")       


 #2. Write a function that safely accesses a dictionary key, catching ValueError KeyError and returning a default value of "Not Found" instead.     
def dictionaryKey(dictionary,key):
    try:
      return dictionary["name":"aamin",
                 "rollno":34,
                 "class"]
    except ValueError:
        return "Not Found"
    except KeyError :
     return "Not found"