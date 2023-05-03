l = [(2, 3), (1, 1), (4, 2), (5, 5), (2, 4)]

# Arrange the above list based on the second element of each item inside the list.
# Result should be [(1,1), (4, 2), (2, 3), (2, 4), (5, 5)]

def get_second_item(data):
    return data[1]


l.sort(key=get_second_item)
print(l)