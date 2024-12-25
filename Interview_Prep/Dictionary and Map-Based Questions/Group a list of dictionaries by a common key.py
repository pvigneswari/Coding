data = [
    {'id': 1, 'name': 'Alice', 'city': 'New York'},
    {'id': 2, 'name': 'Bob', 'city': 'Los Angeles'},
    {'id': 3, 'name': 'Charlie', 'city': 'New York'},
    {'id': 4, 'name': 'David', 'city': 'Chicago'},
    {'id': 5, 'name': 'Eve', 'city': 'Los Angeles'}
]


def groupByKey(data,key):
    grouped_Data ={}
    for item in data:
        grouped_value=item[key]
        if grouped_value not in grouped_Data:
            grouped_Data[grouped_value]=[]
        grouped_Data[grouped_value].append(item)

    return grouped_Data

grouped=groupByKey(data,'city')
for city, entries in grouped.items():
    print(f'{city}:{entries}')

