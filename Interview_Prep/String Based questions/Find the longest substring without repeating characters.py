def length_of_longest_substring(s):
    max_length = 0
    
    # Loop over each character as a potential start of a substring
    for i in range(len(s)):
        seen_chars = set()
        current_length = 0
        
        # Build the substring starting from index `i`
        for j in range(i, len(s)):
            if s[j] in seen_chars:
                break  # Stop if we encounter a duplicate character
            
            # Add the character to the set and increment the current length
            seen_chars.add(s[j])
            current_length += 1
        
        # Update the maximum length found so far
        max_length = max(max_length, current_length)
    
    return max_length
s='abcdabcd'
print(length_of_longest_substring(s))  # Output: 4

# def lengthoflongestsubstring(s:str) -> int:
#     max_length = 0
#     for i in range(len(s)):
#         seen_chars = set()
#         current_length = 0
#         for j in range(i, len(s)):
#             if s[j] in seen_chars:
#                 break
#             seen_chars.add(s[j])
#             current_length +=1
#         max_length=max(max_length,current_length)
#     return max_length
# s='abcdefghadvcf'
# print(lengthoflongestsubstring(s))