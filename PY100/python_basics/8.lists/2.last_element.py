# Write a function that returns the last element of a list provided as an argument. For example:
def last(list):
    if list:
        return list[-1]

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))  # None