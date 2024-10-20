class multipliction:
    
    def __init__(self,numbers):
        
        self.numbers=numbers


    def mul(self):
       for i in self.numbers:
           if i %2==0:
              print(f'{i}x8 ={i*8}')
           else:
               print(f'{i}x9={i*9}')  

m1=multipliction(range(1,11))
print(m1.mul())


