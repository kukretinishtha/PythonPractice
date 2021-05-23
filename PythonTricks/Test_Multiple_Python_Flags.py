'''
Different ways to test multiple
flags at once in Python
'''

x, y, z = 0, 1, 0

# Test 1
if x == 1 or y == 1 or z == 1:
    print('passed')

# Test 2
if 1 in (x, y, z):
    print('passed')


'''
These only test for truthiness
'''
# Test 3
if x or y or z:
    print('passed')

# Test 4
if any((x, y, z)):
    print('passed')
