# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

number = 4936
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number % 100) // 10
ones = number % 10

print(f"Ones place is {ones}")
print(f"Tens place is {tens}")
print(f"Hundreds place is {hundreds}")
print(f"Thousands place is {thousands}")
