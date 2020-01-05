"""
Examples from, adaptations of, and responses to:
https://pymotw.com/3/collections/namedtuple.html
"""

import collections

def print_tuple(tpls):
    print('\nFields by index:')
    for p in tpls:
        print('{} is a {} year old {}'.format(*p))

print('-- basic tuples --\n')

bob = ('Bob', 30, 'male')
jane = ('Jane', 29, 'female')

print('Representation:', bob)
print('\nField by index:', jane[0])
print_tuple([bob, jane])

print('\n-- named tuples --')

Person = collections.namedtuple('Person', 'name age gender')

bob = Person(name='Bob', age=30, gender='male')
jane = Person(name='Jane', age=29, gender='female')

print('\nRepresentation:', bob)
print('\nField by name:', jane.name)
print_tuple([bob, jane])

print('\n-- use `rename=True` to avoid errors from reserved words and duplicates --')
with_class = collections.namedtuple(
    'Person', 'name class age',
    rename=True)

print(with_class._fields)

print('\n-- other misc. --\n')
jane_dict=jane._asdict()
print('As dict:', jane_dict)
jane_dict['name'] = 'Janet'
print('If we create a new object of ordered dict, we can mutate it:\n', jane_dict)

janet = jane._replace(name='Janet')
print('\nReplace, aka construct new object with alternate field(s):\n', janet)
