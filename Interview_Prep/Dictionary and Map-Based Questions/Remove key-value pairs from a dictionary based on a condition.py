data = {
    'bob' : 25,
    'joy' : 30,
    'smith' : 35,
    'john' : 40
}

filtered_data = {}
for key,value in data.items():
    if value <= 25:
        filtered_data[key]=value

print('original_data', data)
print('filtered_data', filtered_data)