class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number=account_number
        self.balance=initial_balance
    
    def deposit(self, amount):
        if amount<0:
            print("Invalid amount")
        else:
            self.balance+=amount
    
    def withdraw(self,amount):
        if amount<self.balance:
            print('insufficient balance')
        else:
            self.balance=self.balance-amount
    
    def get_balance(self):
        return self.balance