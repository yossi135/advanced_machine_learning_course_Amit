class DID:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def dividors(self):
         a=min(self.num1,self.num2)
         list=[]

         for i in range(1,a+1):
             if self.num1 %i ==0 and self.num2 % i==0:

                  list.append(i)
         return list

D1=DID(10,20)
print(D1.dividors())