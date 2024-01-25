my_list = [0, 1, 7, 2, 4, 8]
if len(my_list) == 1:
    result = my_list[0] ** 2
elif len(my_list) == 0:
    result = 0
else:
    result = sum(my_list[::2]) * my_list[-1]
print(result)