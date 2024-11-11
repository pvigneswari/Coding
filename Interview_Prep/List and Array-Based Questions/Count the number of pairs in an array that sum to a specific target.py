#Hash map method

def countOfpairstarget(arr,target):
    count =0
    freq = {}
    for num in arr:
        complement = target-num
        if complement in freq:
            count+= freq[complement]
          
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return count
print(countOfpairstarget([1,2,1,3,2,1,4,6],5))

    




#two pointers method
# def numberOfpairs(arr,target):
#     arr.sort()
#     left,right=0,len(arr)-1
#     count=0
#     while left<right:
#         currentSum=arr[left]+arr[right]
#         if currentSum==target:
#             count+=1
#             left+=1
#             right-+1
#         elif currentSum<target:
#             left+=1
#         else:
#             right-=1
#     return count
# print(numberOfpairs([2,4,1,5,6,0],6))#output:3
            