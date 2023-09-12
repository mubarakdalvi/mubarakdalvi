class Account:
    def __init__(self):
        self.account_number = None
        self.account_type = None
        self.balance = 0
        self.transaction = None
    def deposit(self,amount):
        self.balance += amount
        print(f'{amount} is amount. current balance is  {self.balance} balance')
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount} is amount and current balance is {self.balance}')
        else:
            print(f'Cannot withdraw {amount} as it is exceed the current balance of {self.balance}.')
    def __str__(self):
        return f'Account Number: {self.account_number} ,Account Type : {self.account_type}, Balance : {self.balance}, Transaction : {self.transaction}'

a1 = Account()
a1.deposit('6000')


