def mostFrequentElement(arr):
    frequent = {}
    for item in arr:
        if item in frequent:
            frequent[item] += 1
        else:
            frequent[item]=1
    maxFrequent = max(frequent, key=frequent.get)
    return maxFrequent

print(mostFrequentElement([2,3,3,4,5,6,7,8]))
        