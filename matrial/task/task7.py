class calculater:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        return self.num1+self.num2
    def sub(self):
       return self.num1+self.num2
    def mul(self):
       return self.num1*self.num2
    def div(self):
       return self.num1/self.num2
c1=calculater(6,7)
print(c1.sum())