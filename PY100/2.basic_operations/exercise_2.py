# extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
number = 4936
ones = number % 10
number = number // 10
tens = number % 10
number = number // 10
hundreds = number % 10
thousands = number // 10

print(
    f"One place is {ones}\n"
    f"Tens place is {tens}\n"
    f"Hundreds place is {hundreds}\n"
    f"Thousands place is {thousands}"
)