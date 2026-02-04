# Using the code below as a starting point, write a while loop that prints the elements of lst at each index and terminates after printing the last element of the list.
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(f"At index {index} element {lst[index]}")
    index += 1

# What would the code output if lst is empty? Why is that?
# nothing will be printed as the condition index < len(lst) is falsy, so the block is never executed.