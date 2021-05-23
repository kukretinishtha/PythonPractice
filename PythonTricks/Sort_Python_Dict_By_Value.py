'''
    Sorting a Python dictionary by its value
'''

# Method 1
array = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
print(sorted(array.items(), key=lambda x: x[1]))

# Method 2
import operator
print(sorted(array.items(), key=operator.itemgetter(1)))

'''
RESULT:
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
'''