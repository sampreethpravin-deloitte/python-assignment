# Python Program to delete the element in nested dictionary
initialDictionary ={5: 'Hi', 6: 'To', 7: 'Hello', 'A': {1: 'welcome', 2: 'For', 3: 'MANGO'}, 'B': {1: 15, 2: 'car'}}
print(initialDictionary)

del initialDictionary['A'][2]
print("Deleted  key from Nested Dictionary is \n",initialDictionary)


