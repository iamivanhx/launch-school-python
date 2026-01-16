# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')  # Product2: The string `113` matches the second case, so the code block is executed, outputting the string `Product2` to the terminal.
bar_code_scanner(142)    # Product not found!: None of the cases matches the value of the integer 142, so it executes the default case, outputting the string `Product not found!` 

