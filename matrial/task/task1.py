
email=input('''please inter your email and contains to 17 (charaters)or(numbers)
          such as(username@domain.domain ending) :  ''')
if len(email)==17:
    
  count=str(email.count('@'))
  if '.' in email and  count=='1':
     print(f'this email ({email}) is valid ')
     username=email[0:7]
     domain=email[8:13]
     domain_ending=email[13:17]

     print(f'username is  ****{username}***')
     print(f'domain is  ***{domain}***')
    
     if domain_ending=='.com':
        print('The domain ending is  ****commercial domain****')     
        
     else:
        print(f'do not know this  ****{domain_ending}****')               
  else:
   print(f'this email ({email}) is invalid')    
else:
    print('error!! please try again')   
     