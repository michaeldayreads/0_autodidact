"""
Examples from and reactions to https://pymotw.com/3/collections/counter.html

The comparision is made to `bag` or `multiset` data structures, which simply means 
using the same key multiple times.
"""

import collections

c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict    :', c)

for letter in 'abcde':
    print('{} : {}'.format(letter, c[letter]))

extremely = collections.Counter('extremely')
print(extremely)
print(list(extremely.elements()))

words = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        words.update(line.rstrip().lower())

print('Most common letters in the dictionary:')
for letter, count in words.most_common(3):
    print('{}: {:>7}'.format(letter, count))

c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print(c1)
print(c2)

print('\nCombined counts:')
print(c1 + c2)

print('\nSubtraction')
print(c1-c2)

print('\nIntersection')
print(c1 & c2)

print('\nUnion')
print(c1 | c2)