# def invertDict(d):
#     return {v: k for k,v in d.items()}
# d={'a':1, 'b':5, 'c':8 ,'d':3}
# result = invertDict(d)
# print(result)

#handling duplicate values

def inverDict(d):
    inverdic={}
    for k,v in d.items():
        if v not in inverdic:
            inverdic[v]=[k]
        else:
            inverdic[v].append(k)
    return inverdic
print(inverDict({'a':1,'b':3,'c':2,'f':1}))