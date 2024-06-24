"""
Loop on a dictionary (or mapping)
"""

# Define a dictionary
d = {'a': 1, 'b': 2, 'c': 3}

# Iterate over the keys
for key in d:
    print(key)

# Iterate over the values
for value in d.values():
    print(value)

# Iterate over the key-value pairs
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

