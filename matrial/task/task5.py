class read_file:
    
     def __init__(self,x):
        self.x=x
    
    
     def counter_word(self):
      num_words=len(self.x.split())
      return num_words
    
    
     def counter_characters(self) :   
       num_characters=len(self.x)
       return num_characters


     def counter_line(self) :   
       num_line=self.x.count('\n')+1
       return num_line
   
   
file_path=r'C:\Users\A plus\Desktop\AMIT\advanced_machine_learning_course_Amit\matrial\task\fi.py'
with open(file_path,'r') as file:
    read=file.read()

r1=read_file(read)
print(f'number of characters is: {r1.counter_characters()}')
print(f'number of lines is: {r1.counter_line()}')
print(f'number of words is: {r1.counter_word()}')