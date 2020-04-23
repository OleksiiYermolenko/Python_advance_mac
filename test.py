my_list = [2, 3, 5, 2, 4, 6, 7, 56, 34, 75, 33, 11, 8, 7]
len_list = len(my_list)
max_list = max(my_list)
my_list_sort = []
while len(my_list_sort) != len_list:
    for item in my_list:
        min_1 = min(my_list)
        my_list_sort.append(min_1)
        my_list.remove(min_1)
print(my_list_sort)
