class math_clss:
     def __init__(self,num1=0,num2=0):
          self.num1=num1
          self.num2=num2
     
     
     def factorial(self): 
         result=1
         for x in range(0,self.num1):
             result*=self.num1-x
         return result   

     def isPrime(self):
          if self.num1==1:
               return '****error please enter num > 1****'
          else:
            for i in range(2, self.num1):
              if self.num1 % i == 0:
                return False
          return True
 

     def dividors(self):
          mn = min(self.num1, self.num2)
          common_dividors = []
          for i in range(1, mn+1):
            if self.num1 % i == 0 and self.num2 % i ==0:
               common_dividors.append(i)
          return common_dividors
     
     def mul(self):
          return self.num1*self.num2
          
     def power2(self):
          return self.num1**2
     
     def sub(self):
          return self.num1-self.num2
     
     def sum(self):
          return self.num1+self.num2
     
          
     def Float_Division(self):
          if self.num2==0:
             return 'Error: Division by zero is not allowed! '
          else:
              return self.num1/self.num2 
     
     def floor_Division(self):
          if self.num2==0:
               return 'Error: division by zero is not allowed! '
          else:
                return self.num1//self.num2

while True:
      
      
      
     input_function = input('Please enter the function name:  ')
     c2 = math_clss(5, 8)

        # Use getattr to dynamically call the method
     if hasattr(c2, input_function):
       result = getattr(c2, input_function)()
       print(result)
     else:
          print("Function not found.")
          
     question=input('again ?(yes or no').lower()
     if  question=='no':
          break
          
     