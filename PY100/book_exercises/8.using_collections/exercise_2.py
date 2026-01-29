# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

my_string  = 'Launch School'
start = my_string.find('c')
print(my_string[start:start + 6])