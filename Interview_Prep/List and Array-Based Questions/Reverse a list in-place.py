# list=[1,4,5,6,3]
# list.reverse()
# print(list)

def reverseList(list):
    left,right = 0, len(list)-1
    while left<right:
        list[left],list[right]=list[right],list[left]
        left += 1
        right -= 1
    
list=[1,2,3,4]
reverseList(list)
print(list)

