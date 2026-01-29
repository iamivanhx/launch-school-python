# What happens when you run the following program? Why do we get that result?
def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# A NameError exception is raised as the variable `foo` has function scope and is not available outside of the function.