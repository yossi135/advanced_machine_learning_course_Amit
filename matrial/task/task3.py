list_words=input('enter words: ').split( )
def count_words():
    unique_word=set(list_words)
    counts={i:list_words.count(i) for i in unique_word}
    return   counts
print(count_words())    