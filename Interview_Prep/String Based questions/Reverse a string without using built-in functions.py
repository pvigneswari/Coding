s='eye'
def reversed_string(s):
    reversed_s =''
    for i in range(len(s) - 1, -1, -1):
        reversed_s += s[i]
    return reversed_s
print(reversed_string(s))