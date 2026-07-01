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