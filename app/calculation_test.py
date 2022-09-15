def add(num1:int,num2:int):
    return num1+num2

def sub(num1:int,num2:int):
    return num1-num2

def mul(num1:int,num2:int):
    return num1*num2

def div(num1:int,num2:int):

    return num1/num2

class BankAccount():
    def __init__(self,starting_bal=0):
        self.balance = starting_bal
    
    def deposit(self,amount):
        self.balance += amount

    def debit(self,amount):
        if amount >self.balance:
            raise Exception("Insufficient Money")
        self.balance -= amount

    def interest(self):
        self.balance *= 1.1
