my_list = [1, 0, 13, 0, 0, 0, 5]
if len(my_list) == 1:
    my_list = my_list
else:
    count_zero = my_list.count(0)
    while 0 in my_list:
        my_list.pop(my_list.index(0))
    else:
        for zero in range(count_zero):
            my_list.append(0)
print(my_list)