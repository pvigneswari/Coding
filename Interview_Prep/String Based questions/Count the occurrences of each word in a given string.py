def count_words(s):
    s=s.lower()
    words=s.split()
    word_counts ={}
    for word in words:
        #remove  punctuation from each word
        word = ''.join(char for char in word if char.isalnum())
        if word:
            if word in word_counts:
                word_counts[word]+= 1
            else:
                word_counts[word] = 1
    return word_counts
s='the peopl are the only124!  ones who can save the world'
print(count_words(s))
