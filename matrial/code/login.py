import random
from prettytable  import PrettyTable 
u='youssif'
p='3333'
class login_class():
    def __init__(self,x,y) :
        self.x=x
        self.y=y

    def Login(self):
    
       while True:
        

        if self.x==u:
            
        
          if self.y==p:
            s=random.randrange(1000,1000000)
            print(f'verification code is :{s}')
            
            while True:
                i=int(input('enter verification code:  '))
            
                if i==s:
                   print('****welcome***')
                   break
                else:
                    print('incorrect verification code: try again')    
            break 
          else:
            print('incorrect password:')
        else: 
         print('incorrect username:')               


