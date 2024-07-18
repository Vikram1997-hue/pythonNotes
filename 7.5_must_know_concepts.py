# Reference: https://www.youtube.com/watch?v=mMv6OSuitWw

#--------------------Mutable vs Immutable-----------------------

'''
Immutables - int, float, str, bool, bytes, tuple

Mutables - list, set, dict, and pretty much any other type you get out of some 3rd party library or module
'''
# Lists are mutable
x = [1,2]
x[0] = 'a'
print(x)

# # The following gives an error, since tuples are immutable
# y = (1,2)
# y[0] = 'a'
# print(y)


# this is fine because I never changed the tuple (1,2) or (2,3). I just changed the variables that point to them
a = (1,2)
b = a
a = (2,3)
print(a)
print(b)


# HOWEVA
arr1 = [1,2]
arr2 = arr1
arr2[0] = 2
print("\n\n", arr1)
print(arr2)
# This tells us that if you say a = <some mutable object> and b = a, any changes to one will affect the other since MUTABLES GET
# COPIED BY REFERENCE. Immutables get copied by value 


# another way to demonstrate the above principle -
def get_nth_largest_number(nums, n):
    nums.sort()
    return nums[-n]

nums = [67,1,1,2,3,4,7,8,21,234]
print(nums)
print(f'2nd largest -> {get_nth_largest_number(nums, 2)}')
print(nums) # the original got sorted, since lists are mutable



#-------------------------------List Comprehensions------------------------------------

print("\n\n")
myList = [i for i in range(10)] # this is a list comprehension for populating a list using a for loop
print(myList)


myList = [[] for i in range(10)]
print(myList)
myList = [[i] for i in range(10)]
print(myList)

myList = [[j for j in range(5)] for i in range(10)]
print("\n", myList)


myList = [i for i in range(10) if i % 2 == 0]
print("NEW--->",myList)


#------------------------------Is the current file the main file?-------------------------------

# This concept seeks to find out if the current file is our, well, server.js

''' Check out __main__. First run file1, then file2. You will find that 'file1 is the main file' will only get printed when you
run file1 (obviously), and not when you run file2 '''

# This check is useful if you sometimes have code that you want to have run only when you run a file directly, not if the file in
# question is being imported
