def removeduplicates(s):
    # seen=set()
    result=[]
    for char in s:
        if char not in result:
            # seen.add(char)
            result.append(char)
    return ''.join(result)
s='swallowuuohyyttrrreeewwww'
print(removeduplicates(s))