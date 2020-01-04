"""
Exercises from, adaptations of, and responses to
https://pymotw.com/3/collections/deque.html
"""

import collections
import threading
import time
import random

d = collections.deque('abcdefg')
print('Deque:', d)
print('Length:', len(d))
print('Left end:', d[0])
print('Right end:', d[-1])

d.remove('c')
print('remove(c):', d)

d1 = collections.deque()
d1.extend('abcdefg')
d1.append('h')
print("Back to original and `append('h')`:", d1)

d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

candle = collections.deque(range(5))

def burn(direction, nextSource):
    while True:
        try:
            next = nextSource()
        except IndexError:
            break
        else:
            print('{:>8}: {}'.format(direction, next))
            time.sleep(0.1)
    print('{:>8} done'.format(direction))
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()

left.join()
right.join()

d = collections.deque(range(10))
print("Normal:\n", d)
d.rotate(2)
print('Rotate +2:\n', d)
d.rotate(-4)
print('Rotate -4:\n', d)

random.seed(1)

d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)

for i in range(5):
    n = random.randint(0, 100)
    print('n = ', n)
    d1.append(n)
    d2.appendleft(n)
    print('d1:', d1)
    print('d2:', d2)

