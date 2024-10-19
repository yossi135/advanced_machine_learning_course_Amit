import random
length=int(input('ENTER THE LEN'))
class guess:
    def __init__(self,length):
         self.lenghth=length
    def generate_password(self):
       characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
       num_of_chars = len(characters)
       password = ""

       for _ in range(length):
           rand_indx = random.randrange(0, num_of_chars)
           password += characters[rand_indx]

       return password
 
        
g1=guess(length)
print(g1.generate_password())

