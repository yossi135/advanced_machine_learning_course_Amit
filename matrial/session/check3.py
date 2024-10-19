str1=input()
str2=input()     
class STRR:
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
           
    def string(self):
        longes_str=''
        for i in range(len(self.str1)):
             for j in range(1,len(self.str1)): 
               slic=self.str1[i:j+1]
               print(slic)
               if slic in self.str2 :
                  if len(slic)>len(longes_str)    :
                    longes_str=slic
        return longes_str
c1=STRR(str1,str2)
print(c1.string())