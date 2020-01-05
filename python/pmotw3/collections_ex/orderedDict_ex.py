"""
Examples from, adaptations of, and responses to:
https://pymotw.com/3/collections/ordereddict.html
"""

import collections
import sys

def dprint(d, note=None):
    for k, v in d.items():
        print(k, v)
    if note:
        print_note(note)

def print_note(note):
    print('\n  Note:', note)

def compare_dicts(d1, d2, note=None):
    print('\nComparing:')
    print('d1:', d1)
    print('d2:', d2)
    print('Equal? {}'.format((d1 == d2)))
    if note:
        print_note(note)

def side_effect_tracking():
    """In versions greater than 3.6, standard dicts have tracking as a side effect."""
    version = sys.version
    major = int(version[0:1])
    minor = int(version[2:3])
    if major >= 3 and minor >= 6:
        return True
    else:
        return False

print('Regular dictionary:')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'

dprint(d)

print('\nOrdered Dictionary:')
od = collections.OrderedDict()
od['a'] = 'A'
od['b'] = 'B'
od['c'] = 'C'

dprint(od, 'The above example is not interesting in versions greater than 3.6.')

od2 = collections.OrderedDict()
od2['c'] = 'C'
od2['a'] = 'A'
od2['b'] = 'B'

od3 = collections.OrderedDict()
od3['c'] = 'C'
od3['a'] = 'A'
od3['b'] = 'B'

compare_dicts(d, od,'In implementations >= 3.6, these might be equal!')
compare_dicts(od, od2)
compare_dicts(od2, od3)

print('Items can be moved to the start or end. Using the same two [od2, od3] from the last example...')

od2.move_to_end('b', last=False)
compare_dicts(od2, od3, "`od2.move_to_end('b', last=False)`")