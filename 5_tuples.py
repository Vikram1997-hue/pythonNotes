names = ('Vikram', "Gowrav", "Karitk", 'Vipin', "Vikram")
print(names)

for name in names:
    print('Hi! I am', name, 'and my type is', type(name))


# names[0] = 'Vikramaditya' # gives an error
print(names.count('Vikram'))
print(names.index('Vikram')) # index of first occurrence of param
# print(names.index('Vikr')) # gives an error because no such element in tuple (same as list)
