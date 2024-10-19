input_file = open(r"C:\Users\A plus\Desktop\AMIT\advanced_machine_learning_course_Amit\matrial\session\jfgh.text", "r")
def count_file(input_file):
    text = input_file.read()
    input_file.close()
    text = text.replace('\n', ' ')
    words = text.split(' ')
    unique_words = set(words)
    word_counts = {word: 0 for word in unique_words}

 
    unique_words = set(words)
    word_counts = {word: 0 for word in unique_words}

      
    for i in unique_words:
       for j in words:
         if i == j:
             word_counts[i] += 1
    output_file = open(r" C:\Users\A plus\Desktop\AMIT\advanced_machine_learning_course_Amit\matrial\session\jkm.text ", "w")
    for word in word_counts:
        output_file.write("{}: {}\n".format(word, word_counts[word]))
        output_file.close()            
count_file(input_file)