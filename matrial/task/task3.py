Encoded_Message='&&&**$gnirtS PLIO!!@1234'
the_core_part=Encoded_Message[6:17]
first_word=Encoded_Message[6:12]
second_word=Encoded_Message[13:17]
print(f'The core message is {the_core_part}')
reverse=first_word[::-1]
print(f'The first word becomes {reverse}')
replace_1=second_word.replace('I','E')
replace_2=replace_1.replace('O','U')
print(f'the final decoded message is {reverse} {replace_2} ')


