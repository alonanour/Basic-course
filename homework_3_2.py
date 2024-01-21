value_list = [12, 3, 4, 10, 8]

if len(value_list) == 0:
    print(value_list)
else:
    value_list.insert(0, value_list[-1])
    value_list.pop()
    print(value_list)