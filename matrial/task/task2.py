class methods:
        def __init__(self,num1,num2):
            self.num1=num1
            self.num2=num2
        def add(self):
          return self.num1+self.num2
        def subtract(self):
           return self.num1-self.num2
        def multiply(self):
         return self.num1 * self.num2
        def divide(self):
          if num2 != 0:
           return self.num1 / self.num2
          else:
            return "Error! Division by zero."      
print("Welcome to the calculator!")
print("Choose an operation:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")
choice = input("Enter the number of the operation you want to perform (1/2/3/4): ")
if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
        c1=methods(num1,num2)      
        
        if choice == '1':
            print(f"{num1} + {num2} = {c1.add()}")
        elif choice == '2':
            print(f"{num1} - {num2} = {c1.subtract()}")
        elif choice == '3':
            print(f"{num1} * {num2} = {c1.multiply()}")
        elif choice == '4':
             print(f'{num1} / {num2} = {c1.divide()}' )              
else:
    print("Invalid choice! Please select a valid operation (1/2/3/4) ")       

      

