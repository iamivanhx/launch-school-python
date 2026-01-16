# What does this code output, and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # Empty: an empty collection is falsy, so the block under the else statement is executed.

