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
     

c2=math_clss(1,8)
print(c2.factorial())
print(c2.dividors())
print(c2.isPrime())