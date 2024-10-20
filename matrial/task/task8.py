class Dividors:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def dividors(self):
        common_dividors=[]
        min_number=min(self.num1,self.num2)
        for i in range(1,min_number+1):
            if self.num2%i==0 and self.num1%i==0:
                 common_dividors.append(i)
        return common_dividors

d1=Dividors(5,20)  
print(d1.dividors())