mydictionary ={}

# dictionary with integer keys
mydictionary = {
    1: 'apple',
    2: 'ball'
}



mydictionary = {
    'name': 'Jack',
    'age': 26
}

# Outnut: Jack
print(mydictionary['name'])
print(mydictionary.get('age'))

# Update value
mydictionary['age'] = 27
print(mydictionary)

# Add info
mydictionary['address'] = 'downtown'
print(mydictionary)

#
mydictionary.pop('age')
print(mydictionary)