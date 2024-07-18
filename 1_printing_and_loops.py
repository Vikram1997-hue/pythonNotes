print('Never made it as a wise man')


# for i in range(1, 6): 
#     print('The value of i--->', i)
#     for j in range(1, 6):
#         print('*')


# for i in range(5):
#     for j in range(0, i+1):
#         print('*', end='')
#     print()

for k in range(1, 11, 2):
    print(k)

print(k)

for i in range(1, 1_001):
    print(i)


for j in range(1, 6):
    print('*' * j)


# # will give an error. each of the 3 params must be integers
# for i in range(1.0, 6, 1):
#     print(i)


# f-strings (formatted string literals)
name = 'Vikram'
age = 26
print(f'My name is {name} and I\'m {age} years old')
