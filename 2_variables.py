# name = 'Vikram'
# name = 'Vukrim' #this is fine
# print(name)


# firstName = 'Vikramaditya'
# is_developer = True
# print(firstName, 'is a developer--->', is_developer)


# if(is_developer):
#     print('Sahi h bhai')
# else:
#     print('To bhi sahi h bhai')




# # input function in python
# # num = input("Please enter a no.: ") #always returns a string. So instead, I'll say -
# num = int(input("Please enter a no.: "))
# print('Your num is', num)
# import math
# isPrime = True

# for i in range(2, int(math.sqrt(num))+1):
#     # print('Result:', i, num%i)
#     if(num % i == 0):
#         isPrime = False
#         break

# print("Number is", {True:'Prime', False:'Not prime'} [isPrime])


# # ------------------------------------------------------------------------------

# num = int(input('Please enter a no.: '))
# print('You have entered:', num)
# import math
# dupl = num
# ans = 0

# while dupl > 0:
#     digit = int(dupl%10)
#     digit **= 3
#     ans += digit
#     dupl = int(dupl/10)

# print('Your number is', {True: 'Armstrong!', False: 'not Armstrong :('} [ans == num])


# -------------------------------------------------------------------------------

# print(10 == 0)
# print(10 == 10)
# print(10 == 10.0000) # NOTE: this is True
# print(10 == 10.0001)


# -------------------------------------------------------------------------------

# In-built conversion functions:
# int(), float(), bool(), str()


# -------------------------------------------------------------------------------

# Datatypes
print(type(12))
print(type(12.0))
print(type(12 + 3j))

