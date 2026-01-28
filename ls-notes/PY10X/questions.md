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

## Flow Control

### Would it be possible for both an `if` block _and_ its accompanying `else` block to be executed in a single execution of the conditional? Why or why not?

### Are there any cases where comparison operators can be used between different types in Python? If so, give an example; if not, explain why.

### How could we replicate the functionality of `<=` with a conditional _without_ using `<=` directly?

### Is the string `'False'` falsy? What about negative numbers—are they falsy? More generally, which strings are falsy, and which integers are falsy?

### When evaluating a logical condition with multiple sub-expressions, is it guaranteed that all sub-expressions will be evaluated? Why or why not?

### Is there anything you can do with a `match/case` statement that you _can't_ do with an `if` conditional? If so, provide an example; if not, explain why.

## Intro to Collections

### What are the two key characteristics that define a collection as a sequence? What are at least two characteristics that can differ between sequence types?

### Could we store an integer _and_ a float of the same value into a set, like `3` and `3.0`? Aren't these two objects considered equal?

### How are sets similar to the _keys_ of a dictionary?

### Why do you think dictionaries require each _key_ to be unique, but allow _values_ to be repeated?

### Why do you think we must use a constructor function to create an _empty_ set?

### When the `step` is large and the next value would overshoot the `stop`, does `range` include that value and then stop, or does it stop before? For example, consider `range(0, 7, 5)`. With this range include `10`, or will it stop before reaching `10`?

### When you pass a mutable collection, like a list, into a constructor such as `tuple()` or `set()`, does this mutate the original collection into a new type, or does it leave the original unchanged? Why or why not?

## Using Collections

### What are two ways to access the last element of a non-empty list in Python when you don't know its length? Write the code for both. Which approach would you typically use, and why?

### Why isn't it possible to use slicing syntax on sets in Python?

### We've seen two main operations above, key-based access, and key-based access with assignment. Are either of these operations mutating? How can we tell?

### How might the `in` operator behave when you check if a list (e.g., `[1, 2]`) is an element within another list? Write a code example that tests or demonstrates how `in` works in this situation.

### Suppose you want to get the index of a certain value in a list, but you don't know if the value is present. What is one way you could safely retrieve the index without causing an error if the value isn't found?

### Dictionary view objects change when the dictionary is updated. What could you do if you want a collection of the dictionary's values that does _not_ change after you collect it?

### What operator or method could you use along with `remove` to ensure you only attempt to remove an element from a list if it exists, thus avoiding an error?

### When using the key argument in `sort` or `sorted`, how does the function or method you provide influence how the list is sorted? What can we imply that Python does with this function as it sorts?

### What's the difference between `capitalize` and `title`?

### Is calling `strip()` with no arguments the same as calling `strip(' ')`? Why or why not?

### How does supplying a tuple as an argument to `startswith` or `endswith` change the behavior of these methods?

### Is calling `split()` with no arguments the the same as calling `split(' ')`? Why or why not?

### What is the main practical difference between using `text.find('x')` and `'x' in text` when searching for a substring, and how might you decide which to use?

### Considering that a tuple can contain objects like lists, what do you think determines whether a tuple itself is hashable?

## Loops & Iterating

### Why do we need to initialize our `counter` _before_ the `while` loop? What would be the consequence of initializing it inside the loop?

```python
counter = 1
while counter <= 1000:
    print(counter)
    counter += 1
```

### How is a `while` loop similar to an `if` conditional? In what important way do they behave differently?

### If you have a task that could be accomplished with either a `for` loop or a `while` loop, which would you choose, and why?

### Is there anything we can do with a `for` loop that we _can't_ do with a `while` loop?

### What's the difference between `break` and `continue`?

### If you need to iterate over three (or more) collections simultaneously, can you still use `zip`? How would the loop's unpacking statement need to change?

### What do lists, dicts, and sets all have in common that likely makes them suitable for being compatible with comprehensions?

## Variables as Pointers

### Should we be concerned about unintended side effects from certain operations when dealing with numbers? Why or why not?

### In summary, what's the difference between two objects being the same and two objects having the same value? What tools can we use to test for each of these characteristics?

### Would creating a shallow copy of a list that contains _only_ immutable objects ever lead to unintended side effects? Why or why not?

### Someone argues that we should _always_ make deep copies of objects to avoid unexpected bugs. How would you respond to this advice?



