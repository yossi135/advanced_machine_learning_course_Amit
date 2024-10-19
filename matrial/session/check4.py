class reverce:
    def __init__(self,s):
        self.s=s

    def fun(self):
      lst = '\t'.join(self.s)
      new_lst = lst[::-1]
    
      new_str = " "
      for i in new_lst:
         new_str += i + " "
         new_str = new_str[:-1]
    
      return new_str
 
 
s = "Hello World"
s1=reverce(s)
print(s1.fun())