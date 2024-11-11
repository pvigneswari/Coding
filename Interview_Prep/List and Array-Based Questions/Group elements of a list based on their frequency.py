def groupElementsListFrequency(arr):
    frequencyCount={}
    for num in arr:
        if num in frequencyCount:
            frequencyCount[num]+=1
        else:
            frequencyCount[num]=1

    groupFrequencyElement={}
    for element,freq in frequencyCount.items():
        if freq not in groupFrequencyElement:
            groupFrequencyElement[freq]=[]
        groupFrequencyElement[freq].append(element)
        
    return groupFrequencyElement

print(groupElementsListFrequency([2,3,2,5,6,5,5,6,6,6])) #output:{2: [2], 1: [3], 3: [5], 4: [6]}
