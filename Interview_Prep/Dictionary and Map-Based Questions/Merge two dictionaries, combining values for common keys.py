def mergeDict(dict1,dict2):
    mergeDic=dict1.copy()
    for key,value in dict2.items():
        if key in mergeDic:
            mergeDic[key]+=value
        else:
            mergeDic[key]=value
    return mergeDic

print(mergeDict({2:3,4:5,6:2},{3:1,4:1,7:1})) #output: {2: 3, 4: 6, 6: 2, 3: 1, 7: 1}