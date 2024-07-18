# # # prime
# # import math
# # num = int(input('Please enter a no.: '))
# # isPrime = True

# # for i in range(2, int(math.sqrt(num)) + 1):
# #     if num % i == 0:
# #         isPrime = False
# #         break

# # print('Your number is', {True: 'prime', False: 'not prime'}[isPrime])



# # Armstrong

# num = int(input("Please enter a no.: "))
# dupl = num
# sum = 0

# while dupl > 0:
#     digit = dupl % 10
#     digit **= 3
#     sum += digit
#     dupl = int(dupl/10)

# print('Your number is', {True: 'Armstrong', False: 'not Armstorng'} [num == sum])


for i in range(5):
    for j in range(0, i+1):
        print('*', end='')
    print()