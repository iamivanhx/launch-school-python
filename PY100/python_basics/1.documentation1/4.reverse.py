# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

# There is no built-in method to reverse a string but:
my_string = 'hello'
print(''.join(reversed(my_string)))
print(my_string[::-1])