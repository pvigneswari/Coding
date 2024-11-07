#Quick sort
#It picks an element as a pivot and partitions the list such that elements less than the pivot are on the left, and elements greater than the pivot are on the right. It then recursively sorts the sublists.

def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left =[]
    right =[]
    for x in arr[:-1]:
        if x<=pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort(left)+[pivot]+quicksort(right)
print(quicksort([2,67,44,31,22]))
