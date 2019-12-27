"""
Examples etc. from https://pymotw.com/3/getpass/index.html
"""

import getpass
import sys

try:
    p = getpass.getpass(prompt='token required:', stream=sys.stderr)
except Exception as err:
    print('ERROR:', err)
else:
    print('You entered:', p)