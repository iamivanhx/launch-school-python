# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# Expected output
# 6
# 4
# 2
# 4
# 16
# 0

outer_idx = 0

while outer_idx < len(my_list):
    inner_idx = 0
    while inner_idx < len(my_list[outer_idx]):
        if my_list[outer_idx][inner_idx] % 2 == 0:
            print(my_list[outer_idx][inner_idx])
        
        inner_idx += 1
    outer_idx += 1