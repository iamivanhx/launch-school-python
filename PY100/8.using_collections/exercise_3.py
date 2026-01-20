# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse order from the original. It should also exclude the first and last members of the original. The result should be the tuple (4, 3, 2).

orig_tuple = (1, 2, 3, 4, 5)
my_list = list(orig_tuple)[1:-1]
my_list.reverse()
my_tuple = tuple(my_list)
print(my_tuple)