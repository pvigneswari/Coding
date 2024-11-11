def sortDictByValue(d,reverse=False):
    # Use sorted() to sort the dictionary by its values
    sortedItems=sorted(d.items(), key=lambda item:item[1],reverse=True)
    # Convert the sorted list of tuples back to a dictionary
    return dict(sortedItems)

print(sortDictByValue({'a':2,'n':5,'c':3}))#output:{'n': 5, 'c': 3, 'a': 2}


