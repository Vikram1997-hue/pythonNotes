names = ["Vikram", "Kartik", "Vipin", "Gowrav", "Tarun"]
print(names, type(names), type(type(names)))
print(names[0])
print(names[3])
print(names[-1] + names[-2])


# sub-sequence
print(names[0:3]) # does not mutate original
print(names)


names.append(2) # allowed
print(names)
names.remove('Vipin') # remove first occurrence of param
print(names)
# names.clear() # purge
# print(names)

print('Vikram' in names)
print(len(names)) # len is a function, not a method

for name in names:
    print('Hi! I am', name)



print(names.index('Vikr')) # gives an error because no such element in tuple
