# Write a function to compress a string (e.g., "aaabb" -> "a3b2"
def compresString(s):
    compress=[]
    count=1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count +=1
        else:
            compress.append(s[i-1]+str(count))
            count  = 1
    compress.append(s[-1]+str(count))
    return ''.join(compress)
s='aab'
print(compresString(s))  # Output: a2b1
