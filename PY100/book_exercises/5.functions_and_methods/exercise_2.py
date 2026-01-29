# What does this program print? Why?
foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)  # bar

# Local variable `foo` shadows the global variable `foo`. Both variables have the same name but are two different variables, one has global scope and the other one has function scope.