print('''Weloce to the simple calculator
      select an operation 
       1- addition(+)
       2- subtraction(-)
       3- multiplication(*)
       4- divition(/)
       5- exit
      ---------------------------''')
def calculater(num1,num2,choose):
     if choose=='1':
         return num1+num2
     elif choose=='2':
         return num1-num2
     elif choose=='3':
         return num1*num2
     elif choose=='4':
         if num2==0:
             return 'Error: Division by zero is not allowed! '
         else:
              return num1/num2 
while True:
    choose=input('Enter your choice (1,2,3,4,5) : ')
    if choose=='5':
        print('********You are out of the calculator******* ')   
        break
    elif choose in ['1','2','3','4']:
       try: 
          num1=float(input('ENTER THE FIRST NUM: '))
          num2=float(input('ENTER THE SECOND NUM: '))
          print(calculater(num1,num2,choose))
       except ValueError:
                         print('please enter number  ')
    else:
        print('ERROR NOT FOUND THIS CHOICE IN LIST')    
    question=input('Are you going to perform another calculation?? (yes Or no)').lower()
    if question=='no' or '':
        break         