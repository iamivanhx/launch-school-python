# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# Because the counter variables is not modified inside the block of the while statement, so it will always reference 0, so the expression counter < 5 is always truthy.