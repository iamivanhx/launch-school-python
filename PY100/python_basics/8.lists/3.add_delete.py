# We are given the following list of energy sources.
# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
print(f"Original list: {energy}")

energy.pop(0)
energy.append('geothermal')

print(f"Mutated list: {energy}")

