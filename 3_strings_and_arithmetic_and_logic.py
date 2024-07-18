# strings in Python are immutable

num = 'Python is an HLL'
print(num.find('x')) # -1 if element not found
print(num.find('Python'))

print('Python' in num) # bool output


print(10 / 3) # for double division
print(10 // 3) # for integer division


# -----------------------Logical Operators-------------------------------

# OR and AND in Python
n = 12
if n < 10 or n > 30:
    print('Out of range')
elif 10 <= n and n <= 30:
    print('In range')
else:
    print('How... did you even accomplish this?')


# NOT in Python
if not n >= 0:
    print('No. is negative')
else:
    print('No. is non-negative')
