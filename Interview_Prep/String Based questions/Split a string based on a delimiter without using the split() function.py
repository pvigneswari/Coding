def splitString(s,delimiter):
    result = []
    current = ''
    for char in s:
        if char == delimiter:
            result.append(current)
            current=''
        else:
            current += char

    result.append(current)

    return  result


print(splitString('apple,orange,lilly', ','))