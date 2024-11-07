def mergedList(list1,list2):
    mergeList = []
    i,j=0,0
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            mergeList.append(list1[i])
            i+=1
        else:
            mergeList.append(list2[j])
            j+=1
    #remainingAppend any remaining elements from list1 or list2
    mergeList.extend(list1[i:])
    mergeList.extend(list2[j:])

    return mergeList

print(mergedList([23,45,78],[45,65,98]))
# print(mergedList([3,4,8],[1,5,2]))