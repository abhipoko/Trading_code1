#exercise

# class Student:
#     division=3
#     dress_code='white'

# student1=Student()
# student2=Student()


# print(student1.dress_code)
# print(student2.division)

# class Car:

#     def __init__(self,c,b,p):
#         self.color=c
#         self.brand=b
#         self.price=p
    
#     def get_price(self):
#         return self.price-self.price*0.1
    
# car1=Car('red','toyata',1700000)
# car2=Car('blue','maruti',1500000)

# print(car2.get_price())


class Bank_Account:

    bank_name='ICICI'
    ifsc_code='ICICI0101'
    
    def __init__(self,account_no, name, balance):
        self.account_no=account_no
        self.name=name
        self.balance=balance

    def credit(self,amount):
        self.balance=self.balance+amount

    def debit(self,amount):
        self.balance=self.balance-amount

    def get_balance(self,amount):
        self.balance=self.balance
    

acct1=Bank_Account(12345,'poko',50)
acct2=Bank_Account(23456,'choco',100)
acct3=Bank_Account(34567,'Koko',10)

acct2.debit(50)
acct2.credit(5000)

print(acct2.bank_name)
print(acct2.ifsc_code)
print(acct2.account_no)
print(acct2.name)
print(acct2.balance)