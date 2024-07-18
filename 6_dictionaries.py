# Dictionary - a collection of {key:value} pairs
#            - ordered and changeable. No duplicates

capitals = {
    'India': 'New Delhi',
    'USA': 'Washington, D.C.',
    'China': 'Beijing',
    'Russia': 'Moscow',
}
print(capitals, type(capitals))

# both work
print(capitals.get('India'))
print(capitals['Russia'])

# if you pass a key that doesn't exist -
print(capitals.get('DPRK'), type(capitals.get('DPRK'))) # output - None. This is not a string, but a special value in Python
# print(capitals['DPRK']) # but this syntax will give an error


# None is a falsy value
if(capitals.get('DPRK')):
    print('That capital exists')
else:
    print('That capital does not exist')


if(None):
    print('Hehe')
else:
    print('Not hehe')

capitals.update({"DPRK": 'Pyongyang'}) # .update() will upsert
capitals.update({'USA': 'Abuja'})
print(capitals)

# to remove -
capitals.pop('DPRK')
capitals.popitem() # detects what the last entry in the dictionary is, and deletes it
print(capitals, len(capitals))


# # to purge -
# capitals.clear()
# print(capitals, len(capitals))


# get all keys
myKeys = capitals.keys()
print(myKeys, len(myKeys), type(myKeys))


# get all values
myValues = capitals.values()
print(myValues, len(myValues), type(myValues))


# get all entries (items)
print("\n\n")
myItems = capitals.items()
for item in myItems:
    print(item, type(item), type(myItems)) # note that each item is a tuple


# now check this out
for key, value in myItems: # destructuring combined with for loop
    print(f'{key} --> {value}')




# Dictionaries can be overwritten
print("\n\n")
capitals = {'UK': 'Dehradun', 'UP': "Lucknow"}
print(capitals)
