def palindrome(word):
    list1=list(word)
    rev = ''.join(list1[::-1])
    return word==rev
print(palindrome('madaml'))
# #another  way to check palindrome
# def isPalindrome(s):

#     # Using predefined function to
#     # reverse to string print(s)
#     rev = ''.join(reversed(s))

#     # Checking if both string are
#     # equal or not
#     if (s == rev):
#         return True
#     return False

# # main function
# s = "family"
# print(isPalindrome(s))


# #another  way to check palindrome

# def palindrome(word):
#     return word == word[::-1]
# print(palindrome('madam'))

# #another  way to check palindrome
# def palindrome(s):
#     cldString = ''
#     for char in s:
#         if char.isalnum():
#             cldString += char.lower()
#     left,right=0,len(cldString)-1
#     while left<right:
#         if cldString[left] != cldString[right]:
#             return False
#         left +=  1
#         right += 1
#     return True

