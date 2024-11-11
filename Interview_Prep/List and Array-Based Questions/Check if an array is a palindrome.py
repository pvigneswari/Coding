#two pointer approach
def arrayPalindrome(arr):
    left,right = 0, len(arr)-1
    while left<right:
        if arr[left]!=arr[right]:
            return False
        left += 1
        right -= 1
    return True
print(arrayPalindrome([2,3,3,2])) #expected output true


# def arrayPalindrome(arr):
#     rev=arr[::-1]
#     return  rev==arr
# # print(arrayPalindrome(['m','a','d','a','m','t']))
# print(arrayPalindrome([1,2,1]))