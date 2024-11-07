def secondLargestElement(arr):
    uniqueArr=list(set(arr)) #remove duplicates
    if  len(uniqueArr)<2:

        return None
    uniqueArr.sort()
    return uniqueArr[-2] #return second largest element
print(secondLargestElement([40,56,89,89,56,40]))