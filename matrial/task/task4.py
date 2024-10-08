Encoded_message='##$$$@!yalpstcejorp EPUVT****9887'
The_core_part=Encoded_message[7:25]
first_word=Encoded_message[7:19]
second_word=Encoded_message[20:25]
reverse=first_word[ : :-1]
replace1=second_word.replace('E','A')
replace2=replace1.replace('U','O')
print(f'''The core part is {The_core_part} 
      the first word becomes {reverse} 
      Final decoded message is {reverse}  {replace2} ''')