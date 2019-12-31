"""
Examples from and reactions to https://pymotw.com/3/collections/chainmap.html
"""

import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)

print('Individual Values')
print('a = {}'.format(m['a']))
print('b = {}'.format(m['b']))
print('c = {}'.format(m['c']))
print()

print('keys = {}'.format(list(m.keys())))
print('values = {}'.format(list(m.values())))
print()

print('Items:')
for k, v in m.items():
    print('{} = {}'.format(k, v))
print()

print('"d" in m: {}'.format(('d' in m)))

print(m.maps)
print('c = {}'.format(m['c']))

m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

m.maps = list(reversed(m.maps))

print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After: {}'.format(m['c']))
m['c'] = 'C'
print('Back to: {}'.format(m['c']))

m_child = m.new_child()

print('parent before:', m)
print(' child before:', m_child)

m_child['c'] = 'E'

print('parent after:', m)
print(' child after:', m_child)

c = {'c': 'E'}

m_next_child = m.new_child(c)

print(m_next_child)

# Having gone through this exercise, its difficult to imagine a use case.
# Addressed at a high level here: https://stackoverflow.com/questions/23392976/what-is-the-purpose-of-collections-chainmap
# Though a real implementation would help. 