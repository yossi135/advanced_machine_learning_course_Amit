str1=input().split(' ')
str2=input().split(' ')
list=[]

class similar_str:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
       
    def give(self):
        
       for i in self.str1:    
         for j in self.str2:
            if j==i:
              list.append(j)
s1=similar_str(str1,str2)
s1.give()
print(list)
