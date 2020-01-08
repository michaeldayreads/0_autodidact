"""
Examples from, adaptations of and reactions to:
https://pymotw.com/3/array/index.html
"""

import array
import binascii
import pprint
import tempfile

s = b'This is the array.'
a = array.array('b', s)

print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))

a = array.array('i', range(3))
print('Initial :', a)

a.extend(range(3))
print('Extended:', a)

print('Slice   :', a[1:3])
print('Iterator:')
print(list(enumerate(a)))

a = array.array('i', range(5))
print('A1:', a)

# write to a file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
# Though we are not opening and closing this file
# nor wrapping it in a context manager it will be closed
# as part of the garbage collection process.
output.flush()

with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read the data into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)

print('-- bytes --')

a = array.array('i', range(5))
print('A1:', a)

as_bytes = a.tobytes()
print('bytes:', binascii.hexlify(as_bytes))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)

print('-- byte swap --')

def to_hex(a):
    chars_per_item = a.itemsize * 2
    hex_version = binascii.hexlify(a)
    num_chunks = len(hex_version)
    for i in range(num_chunks):
        start = i * chars_per_item
        end = start + chars_per_item
        yield hex_version[start:end]

start = int('0x12345678', 16)
end = start + 5
a1 = array.array('i', range(start, end))
a2 = array.array('i', range(start, end))
a2.byteswap()

fmt = '{:>12} {:>12} {:>12} {:>12}'
print(fmt.format('A1 hex', 'A1', 'A2 hex', 'A2'))
print(fmt.format('-' * 12, '-' * 12, '-' * 12, '-' * 12))
fmt = '{!r:>12} {:12} {!r:>12} {:12}'
for values in zip(to_hex(a1), a1, to_hex(a2), a2):
    print(fmt.format(*values))

