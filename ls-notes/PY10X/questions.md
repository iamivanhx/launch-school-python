# Questions

## Prep

### What is the most important factor that determines how your Python code behaves: the operating system, the editor, or the version of Python installed? Explain your reasoning.

https://launchschool.com/books/python/read/preparations

### How does Python determine where a block of code ends? What specifically signals to Python that the block is complete?

https://launchschool.com/books/python/read/using_python

### When using the Python REPL, what does it mean if your prompt changes from `>>>` to `...` after you press Enter? What can we assume we should do next?

https://launchschool.com/books/python/read/using_python

### In what situations might using the REPL be more convenient than running code from a file? When might it make more sense to use a file instead of the REPL?

https://launchschool.com/books/python/read/using_python

### In theory, what will happen when you run your Python code if you don't follow these style guidelines? Will Python raise an error, why or why not?

https://launchschool.com/books/python/read/using_python

## Data Types

### Is every primitive in Python an object? Is every object in Python a primitive? Explain your reasoning.

https://launchschool.com/books/python/read/data_types#datatypes

### Consider the expression `3 + 2`. When we _execute_ this code, how many literals are involved? How many integers are involved? Explain why.

https://launchschool.com/books/python/read/data_types#datatypes

### Can every reasonably small integer (like ones you'd typically use in programs) be represented as a float? How about vice versa? Why or why not?

https://launchschool.com/books/python/read/data_types#datatypes

### What's the minimum number of objects we must have in our program if we're going to reassign a variable? Why?

https://launchschool.com/books/python/read/data_types#datatypes

### Based on Python's treatment of strings, what arguments could you make both _for_ and _against_ calling a string a collection?

https://launchschool.com/books/python/read/data_types#datatypes

### If we know the length of a string, how could we access the first character of the string _without_ using `my_string[0]`?

https://launchschool.com/books/python/read/data_types#datatypes

### How would you describe the difference in meaning between `False` and `None`?

https://launchschool.com/books/python/read/data_types#datatypes

### Do you expect negative indexing to work with lists and tuples in the same way it works with strings? Why or why not?

https://launchschool.com/books/python/read/data_types#datatypes

### Give an example of a situation where a dictionary would be a better choice than a list. Conversely, describe a case where a list would be more appropriate than a dictionary.

https://launchschool.com/books/python/read/data_types#datatypes

### How are sets different from lists? How are they the same?

https://launchschool.com/books/python/read/data_types#datatypes

## Basic Operations

### If you perform arithmetic operations involving both integers and floats, what type of value is returned? Why do you think Python behaves this way?

https://launchschool.com/books/python/read/basic_ops

### Your banking app currently stores currency amounts in dollars using float values, which leads to precision issues. What alternative representation, using a different unit or data type, could help you avoid floating point errors?

### What's the _return type_ of all comparison operators?

### Do you think you should explicitly convert the integer to a float before performing the operation `1 + 3.5`? Why or why not?

### Why might you choose to use `repr` instead of `str` when printing values while debugging a program that uses both number types and strings containing digits?

### In the code below, why did assigning `my_list[2] = 6` update the `3` to `6` (resulting in `[1, 2, 6, 4]`) instead of updating the `2`?

```python
my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)          # [1, 2, 6, 4]
my_list[4] = 10
# IndexError: list assignment index out of range
```

### Can a statement contain an expression? Can an expression contain a statement? Explain your reasoning.

### When we pass a function invocation into `print`, what are we printing?

## Variables

### Once we reassign `foo` to `'Hello'`, do we have any way to access the string `'abcdefghi'`? Why or why not?

```python
foo = 'abcdefghi'
foo = 'Hello'
```

### Can you give an example of a value in a program that you would want to define as a constant? Why might you want it to remain unchanged?

### Can the left side of the `=` operator be an expression? Why or why not?

### Does augmented assignment ever change the data type of the variable? Why or why not?

### If integers are immutable, how can `my_list[1] = 42` be considered a mutating action?

## Input/Output

### What do you think we would've seen output by `personalized_greeting.py` if the user had hit enter/return without typing anything first?

```python
name = input("What's your name?\n")
print(f'Good Morning, {name}!')
```

### What happens in our `sum_numbers.py` program if a user enters something that _isn't_ a number? How come?

```python
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')
```


## Functions and Methods

### What's one reason we might define a function even if we only intend to use it once?

### When you run `print(print(42))`, both `42` and `None` are logged to the console. Which one appears first, and what does each line represent? Explain why they are printed in that order.

### What's one way we can learn about a built-in function _besides_ looking at the documentation?

### Could two objects that have different ids ever have the same value? Why or why not?

### If we see a variable being referenced, where should we look in our code to determine whether that variable is in scope?

### What's the benefit of passing arguments into functions, rather than defining the needed values as variables within the function body?

### In the `is_digit` function, why are we able to simply `return False`? Why don't we need to use a conditional like `if char < '0' or char > '9'` _before_ returning `False`?

```python
def is_digit(char):
    if char >= '0' and char <= '9':
        return True

    return False
```

### If we see a method we aren't familiar with being used in a code snippet, where should we look in the documentation to find information about it?
