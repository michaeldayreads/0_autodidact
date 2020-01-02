"""
Examples from and responses to https://pymotw.com/3/collections/defaultdict.html
"""

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

# attempting to create something more concrete

def book_details():
    details = {
        'Author': 'Not Provided',
        'Published': 'Not Provided'
    }
    return details

library = collections.defaultdict(book_details)
print(library)
print(library['Zen and the brain'])
print(library)

# from python docs

s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

print(d)
print(sorted(d.items()))