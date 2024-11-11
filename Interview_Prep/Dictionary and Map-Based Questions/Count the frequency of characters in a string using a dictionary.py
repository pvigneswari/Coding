def countFrequency(str):
    fre={}
    for char in str:
        if char in fre:
            fre[char]+=1
        else:
            fre[char]=1
    return fre

print(countFrequency("helloworld5677")) #output:{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1, '5': 1, '6': 1, '7': 2}