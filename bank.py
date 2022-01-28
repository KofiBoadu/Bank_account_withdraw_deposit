


#Designing a bank account login and account creation and withrawal 

class Bank():
    
    def __init__(self):
        
        self.balance= 0
        
        
        
    def Deposit(self):
        
        amount= int(input("how much do you want to deposit?: "))
        
        self.balance= self.balance + amount
        
        print(f"You deposited= {self.balance}.00")
        
        
    
    def Withdraw(self):
        
        amount= int(input("How much do you want to withdraw?: "))
        
        self.balance= self.balance-amount
        
        print(f"You withdrawn={amount}.00")
        
        
        
    def makeEnquiry(self):
        
        print(f" Your balance left now= {self.balance}.00")
        
        













