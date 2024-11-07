def removeDuplicate(list1):
    uniqueList=[]
    for item in list1:
        if item not in  uniqueList:
            uniqueList.append(item)
        else: 
            continue

    return uniqueList

print(removeDuplicate([1,2,3,3,4,2,5]))
