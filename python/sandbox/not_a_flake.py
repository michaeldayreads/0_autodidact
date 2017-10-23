'''Module to test acceptable flake8 formats.'''

test = dict()
test['foo']='baz'
test['bar']={'bux':'qux', 'blam': {'spam':'shazam'}}

data = test['bar']\
        ['blam']['spam']

print data
