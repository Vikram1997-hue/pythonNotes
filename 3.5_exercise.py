weight = float(input('Weight: '))
unit = input('(K)g or (L)bs: ').lower()

if unit == 'l':
    print('Weight in Kg:', weight/2.205)
elif unit == 'k':
    print('Weight in Lbs:', weight*2.205)
else:
    print('Invalid unit entered')
