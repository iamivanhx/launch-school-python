# You need to write some Python code to determine the country name associated with one of the listed names. Your code should include the data structure(s) you need and at least one test case to ensure the code works.

my_dict = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

for key, value in my_dict.items():
    print(f"{key} is from {value}")