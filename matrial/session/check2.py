class prime:
     def  __init__(self):
          print('hello')

     def isprime(self,num):
       for i in range(2,num):
        if     num % i==0 :
            return False

       return True
p1=prime()   
print(p1.isprime(5))