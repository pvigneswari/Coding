dict1 = {'bob' : 21, 'smith':23}
dict2 = {'bob' : 21, 'smith':23, 'john':25, 'jane':26}
isSubset=True
for key,value in dict1.items():
    if key not in dict2 or dict2[key]!=value:
        isSubset=False
        break

print('is dict1 subset of dict2', isSubset)