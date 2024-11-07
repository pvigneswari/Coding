def intersectionOfList(list1,list2):
    return list(set(list1) & set(list2))
print(intersectionOfList([1,3,4,2],[5,6,4,2,8]))




# In this case:

# set(list1) becomes {1, 2, 3, 4}
# set(list2) becomes {3, 4, 5}
# The intersection {3, 4} is converted back to a list, resulting in [3, 4].