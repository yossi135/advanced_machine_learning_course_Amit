Encoded_Message='###!!@emocleW EPGTQ!!!6789'
the_core_part=Encoded_Message[6:13]
print(f'the core part of message is  ****{the_core_part}****')
reverse=the_core_part[ : :-1]
print(f'the first word becomes {reverse}')
new_word=Encoded_Message[14:19]
new_word.replace('E','')
print(f'the final message is {reverse} {new_word}')
