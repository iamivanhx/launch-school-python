# The destinations list contains a list of travel destinations.
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

# Write a function that, without using the built-in in operator, checks whether a specific destination is included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected return value is True, whereas the expected return value for 'Nashville' is False.
def contains(city, destinations):
    if destinations:
        for cty in destinations:
            if city == cty:
                return True
            
    return False

print(contains('Barcelona', destinations)) # True
print(contains('Nashville', destinations))  # False