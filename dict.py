#Adding and Updating Elements
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['gender'] = 'Male'
my_dict['age'] = 32
print(my_dict)


## Checking if a key exists in a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

if 'age' in my_dict:
    print("Age is present in the dictionary")
else:
    print("Age is not present in the dictionary")

## Iterating over a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterating over keys
print("Keys:")
for key in my_dict:
    print(key)

# Iterating over values
print("\nValues:")
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(key, ":", value)
