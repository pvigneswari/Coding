def findPermutations(s):
    if len(s)<=1:
        return  [s]

    perms=[]
    for i in range(len(s)):
        char = s[i]
        remainingPrem=findPermutations(s[:i]+s[i+1:])
        for prem in remainingPrem:
            perms.append(char+prem)
    return perms
print(findPermutations("abc"))
