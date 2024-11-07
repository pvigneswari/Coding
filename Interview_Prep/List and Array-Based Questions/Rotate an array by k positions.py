def roateArray(arr,k):
    k = k%len(arr)   #for cases when k is greater than the length of array
    roateArray = arr[-k:]+arr[:-k]   #extracts the last k elements of arr.[-k:]
    arr[:-k]                           #extracts the elements from the beginning up to (but not including) the last k elements.[:-k]
    return roateArray

print(roateArray([1,2,3,4,5],1))