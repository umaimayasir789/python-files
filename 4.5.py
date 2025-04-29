class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")
    def display_balance(self):
        print("Balance:", self.balance)  
account = BankAccount("John Doe", 1000) 
account.display_balance() 
account.deposit(500)  
account.display_balance()
account.withdraw(200)  
account.display_balance()                    
