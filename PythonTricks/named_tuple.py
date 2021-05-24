from collections import namedtuple

# Returns a new subclass of tuple with named fields.

Point = namedtuple('Point', ['x', 'y'])
print(Point.__doc__)                   # docstring for the new class
p = Point(11, y=22)                    # instantiate with positional args or keywords
print(p)
print(p[0] + p[1])                     # indexable like a plain tuple
x, y = p                               # unpack like a regular tuple
print(x, y)
print(p.x + p.y)                       # fields also accessible by name
d = p._asdict()                        # convert to a dictionary
print(d)
print(d['x'])
print(Point(**d))                      # convert from a dictionary
print(Point(x=11, y=22))
print(p._replace(x=100))               # _replace() is like str.replace() but targets named fields
print(Point(x=100, y=22))