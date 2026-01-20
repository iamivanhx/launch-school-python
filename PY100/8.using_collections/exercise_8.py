# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# On line 5, a new string is returned 'for the fjords', so the index numbers are different than on line 6, in which the counting is done on the original string.

