def kSmallestLargest(arr,k):
    sortedArr=sorted(arr)
    if k<=0 and k>len(arr):
        return "Invalid input"
    smallArr=sortedArr[k-1]
    largestArr=sortedArr[-k]
    return smallArr,largestArr

print(kSmallestLargest([1,4,2,3,56,43,66],3))