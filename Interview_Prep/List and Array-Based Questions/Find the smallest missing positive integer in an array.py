def find_smallest_missing_positive(arr):
    n = len(arr)
    
    # Step 1: Place each number in its correct position if possible
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap arr[i] with arr[arr[i] - 1] to place it in the correct position
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
    
    # Step 2: Find the first missing positive integer
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    
    # Step 3: If all positions are correct, return the next integer
    return n + 1
print(find_smallest_missing_positive([1,2,0]))


# won't work for  this case: [1,2,0] because it will return 3 instead of 3
# l=[1,2,0]
# for i in range(min(l),max(l)+1):
#     if  i not in l: 
#         print(i)
#         break
