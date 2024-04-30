customer_collection = {}
import csv

class Account:
    def __init__(self, account_id,balance, interest = 0):

        if not isinstance(account_id,str):
            raise TypeError('Account ID must be string')    
        for id in account_id:
            if id not in str(list(range(0,10))):
                raise ValueError('Account ID must be within 0-9')
        # if not isinstance(balance,(int,float)):
        #     raise TypeError('Balance must be int or float') 
        self.account_id = account_id
        self.balance = float(balance)
        self.interest = interest

    def __str__(self):
        return f'{self.account_id},{round(float(self.balance),2)},{self.interest}'

    def _withdraw_(self):

        deducted_amount = float(input())

        try:
            self.balance -=  deducted_amount
            if self.balance < 0:
                raise ValueError()
        except ValueError:
            print('Cannot proceed your withdrawal')
            self.balance += deducted_amount
    
class Checking(Account):

    def __init__(self,account_id,balance,interest):
        super().__init__(account_id,balance,interest)
        self.interest = 0
    
    def __str__(self):
        return f'{self.account_id}  {round(float(self.balance),2)}'

class Savings(Account):
    def __init__(self,account_id,balance,interest):
        super().__init__(account_id,balance,interest)
        self.interest = 1
    
    def __str__(self):
        return f'{self.account_id} {round(float(self.balance),2)}'
    
'''for Credit class'''
def __credit_card_charge__(self):

    increased_amount = float(input())

    try:
        self.balance += increased_amount
        if increased_amount > self.limit:
            raise ValueError()
    except ValueError:
        print('You have passed your credit limit')
        self.balance -= increased_amount



def import_account():
    global customer_collection
    step1 = input("which file do you want to access to?")
    with open(f'{step1}', 'r') as readfile:
        account = csv.DictReader(readfile)
        for row in account:
            checking_object = Checking(row['checking_id'], row['checking_balance'], '0')
            saving_balance = Savings(row['savings_id'], row['savings_balance'], '0')
            credit = Credit(row['credit_id'], row['credit_balance'], row['credit_limit'], '0')
            customer = Customer(row['username'], checking_object, saving_balance, credit, '0')
            customer_collection[row['username']] = customer
        print(customer_collection)
        
import_account()


    
            
            
            
        