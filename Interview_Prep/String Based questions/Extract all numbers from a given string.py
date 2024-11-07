def extractNumber(s):
    numbers=[]
    currentNumber = ''
    for char in s:
        if char.isdigit():
            currentNumber += char
        else:
            if currentNumber:
                numbers.append(currentNumber)
                currentNumber =''
    if  currentNumber:
        numbers.append(currentNumber)
    return numbers
s=('10tenten100')
print(extractNumber(s))
# If you want the numbers as integers, you can convert them with list(map(int, extract_numbers(s)))
print(list(map(int, extractNumber(s))))
    