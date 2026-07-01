class Bank:
    #Constructor:Automatically called when obhect is created 
    def __init__(self):
        #Private Instance Variable
        #Initial balance is set to 5000
        #Double underscore(__) makes it private(name)
        self.__balance = 5000
    #Created a method to deposit maoney into the account          
    def deposit(self,amount):
    #Add deposit money account    

        self.__balance += amount
    #Display the current balance 
    def show_balance(self):
        print(f"Current balance: {self.__balance}")        

b = Bank()
b.deposit(6000)
b.show_balance()       






#Define the parent class to holw general data

class Vehicle:
    #The initiator method runs automatically when an object is created
    def __init__(self,brand,year):
       self.brand = brand  #public attribute for the vehicle's brand. Stores in instance variable
       self.year = year #Public sttribute for the vehicles manufacturing year  


    #A method that format and restores teh vehicle details as a  string        
    def display_info(self):
       return f"{self.brand}({self.year})"
    
 #Define a class car Vehicle   that automaticall inherits from the parent class vehicle
class Car(Vehicle):
    #"Pass" is a placeholder showing the vehicle information is inherited from the parent class
    pass   


#Create an object of the Car class 
#then automatically call teh __init__ method inherited from the vehicle 
my_car = Car("toyota",2020)
#calling the display info method inherited from the parent class vehicle 
print(my_car.display_info())



