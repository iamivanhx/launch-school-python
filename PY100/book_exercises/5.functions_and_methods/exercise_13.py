# Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42) # it raises an exception as the thirs parameter is expected to have a default value, as the second parameter has it. Once a parameter has a default value, the subsequent parameters must have one as well.
