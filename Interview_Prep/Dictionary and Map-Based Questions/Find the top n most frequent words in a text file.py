def top_n_frequent_words(file_path, n):
    word_count = {}  # Dictionary to store the word frequency

    # Read the text file and count word frequencies
    with open(file_path, 'r') as file:
        for line in file:
            # Normalize the line: convert to lowercase and split into words
            words = line.lower().split()
            
            # Count the frequency of each word
            for word in words:
                # Optionally remove punctuation
                word = ''.join(char for char in word if char.isalnum())
                if word:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

    # Find the top n most frequent words by sorting the dictionary items
    top_words = []
    for _ in range(n):
        if word_count:
            max_word = max(word_count, key=word_count.get)  # Find the word with the highest frequency
            top_words.append((max_word, word_count[max_word]))  # Append the word and its frequency
            del word_count[max_word]  # Remove it from the dictionary

    return top_words

# Example usage
file_path = 'C:\workplace\coding\Interview_Prep\Dictionary and Map-Based Questions\sample.txt.txt'  # Replace with your file path
top_n = 5  # Number of top frequent words to find
result = top_n_frequent_words(file_path, top_n)
print(result)  # Output: [('word1', count1), ('word2', count2), ...] 
               #[('hello', 2), ('world', 2), ('this', 1), ('is', 1), ('a', 1)]
