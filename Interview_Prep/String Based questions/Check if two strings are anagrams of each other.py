
def anagram(str1,str2):
    if len(str1) !=  len(str2):
        return False
    count1 = {}
    count2 = {}
    for char in  str1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    for  char in str2:
        if char in count2:
            count2[char]  += 1
        else:
            count2[char] = 1
    return  count1 == count2
str1 = 'listen'
str2 = 'silent'
print(anagram(str1,str2)) # False


#without using dictionaries
# Test the function
def are_anagrams(str1, str2):
    # If lengths are different, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Create a count array of size 26 for each letter in the alphabet
    count = [0] * 26

    # Increment count based on characters in the first string
    for char in str1:
        index = ord(char) - ord('a')  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25
        count[index] += 1

    # Decrement count based on characters in the second string
    for char in str2:
        index = ord(char) - ord('a')
        count[index] -= 1

    # If all values in count are zero, the strings are anagrams
    for c in count:
        if c != 0:
            return False

    return True

# Test the function
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))  # Output should be True




