def helloWorld():
    print('Hello world!')

helloWorld()


import math
def isPrime(num):
    ans = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            ans = False
            break
    return ans

num = 14
print(f'The number {num} is', {True: 'prime', False: 'not prime'} [isPrime(num)])




# 2 types of arguments - FUNCTIONAL and KEYWORD




''' If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the 
function definition. This way the function will receive a tuple of arguments, and can access the items accordingly '''
# This syntax is called 'ARBITRARY ARGUMENTS'

def rollcall(*students):
    print(f'Roll number 1 is {students[0]}')
    print(f'Total no. of children = {len(students)}')

print("\n\n")
rollcall('Vikram', 'Kartik', 'Vipin')


# Common use-case: rest syntax
def rollcallz(student1, student2, *students):
    print(f'First student: {student1}')
    print(f'Second student: {student2}')
    print(f'Every other student: {students}')

print('\n')
rollcallz('A', 'B', 'C', 'D', 'E', "F")



# keyword arguments
# using these, the order of arguments does not matter
def rollcall2(student1, student2, student3):
    print(f'First student is {student1}')
    print(f'First student is {student2}')
    print(f'First student is {student3}')

print('\n')
rollcall2(student3='Kartik', student2='Vipin', student1='Vikram')



# arbitrary keyword arguments (use 2 stars)
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def rollcall3(**student):
    print('The first student is', student.get('student1'))

print("\n\n")
rollcall3(student3='Kartik', student2='Vipin', student1='Vikram')




# What if I wanna use some positional and some keyword arguments?
def myFunc(x,y,z):
    print("XYZ:", x, y, z)

myFunc(1, z = 2, y = 3) #then I first must write all my positionals, and then my keywords





# Arbitrary positional and arbitrary keyword args together
def myFunc2(*args, **kwargs):
    print(args)
    print(kwargs)

myFunc2(1,2,3,4, five=5, six=6, seven=7) # as is standard for positionals and keywords together in one call, 
                                         # all positionals must come first, then all the keywords



# we can (kinda) use spread syntax using * and **
def myFunc3(a, b, c = True, d = False):
    print(a, b, c, d)

myFunc3(*(1, 2), **{'c': 'Hello', 'd': 'World'}) # once again, first all the positionals, then all the keywords
# NOTE: it can be [1,2] or (1,2) in the function call - both will work
