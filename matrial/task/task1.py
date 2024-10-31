class bankAccount:
    def __init__(self,balance) :
        self.balance=balance
        
    
    def deposit(self,amount):
          #nonlocal balance
          self.balance += amount
          print(f'Deposited {amount}. New balance: {self.balance}')

    def withdraw(self,amount):
           #nonlocal balance
           if amount > self.balance:
             print('Insufficient funds')
           else:
             self.balance -= amount
             print(f'Withdrew {amount}. New balance: {self.balance}')

    def check_balance(self):
          print(f'Current balance: {self.balance}')

      
initial_balance=float(input('please enter initial balance: '))
deposit_amount=float(input('please enter deposit amount: '))
withdraw_amount=float(input('please enter withdraw amount: '))
    
if deposit_amount < 0 or withdraw_amount < 0:
     print('****Error! Please enter a number greater than zero for deposit or withdraw amount.*****')

else:
    c1=bankAccount(initial_balance)
    c1.deposit(deposit_amount)
    c1.withdraw(withdraw_amount)
    c1.check_balance()

