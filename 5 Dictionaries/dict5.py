# Original Dictionary
fav_numbers = {'eric': 17, 'ever': 4}

# Displaying Original Values
print("Original Values:")
for name in fav_numbers.keys():
    print(name + ' loves ' + str(fav_numbers[name]))

# Changing values
fav_numbers['eric'] = 23
fav_numbers['ever'] = 9

# Displaying Modified Values
print("\nModified Values:")
for name in fav_numbers.keys():
    print(name + ' loves ' + str(fav_numbers[name]))
