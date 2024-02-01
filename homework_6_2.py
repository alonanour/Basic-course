my_dict_1 = {1: 12, 2: 2, 3: 34, 5: 56, 6: 67}
my_dict_2 = {1: 11, 2: 2, 4: 44, 5: 55, 7: 77}

my_set_1 = set(my_dict_1)
my_set_2 = set(my_dict_2)

common_keys_list = list(my_set_1.intersection(my_set_2))
different_keys_list = list(my_set_1.difference(my_set_2))

my_dict_3 = {}
for key, value in my_dict_1.items():
    if key in my_dict_2:
        continue
    else:
        my_dict_3[key] = value

my_dict_4 = {}
for key, value in my_dict_1.items() | my_dict_2.items():
    if my_dict_1.get(key) == my_dict_2.get(key):
        my_dict_4[key] = my_dict_1.get(key)
    elif key not in my_dict_2:
        my_dict_4[key] = my_dict_1.get(key)
    elif key not in my_dict_1:
        my_dict_4[key] = my_dict_2.get(key)
    elif key in (my_dict_1 and my_dict_2):
        my_dict_4[key] = [my_dict_1.get(key), my_dict_2.get(key)]

print(f"A list of keys that are in both dictionaries: {common_keys_list}"
      f"\nA list of keys that are in the first dictionary but not in the second: {different_keys_list}"
      f"\nA dictionary of key-value pairs that are in the first dictionary but not in the second: {my_dict_3}"
      f"\nA dictionary of two combined dictionaries: {my_dict_4}")