try:
    baz = 'foo''
    raise TypeError
except Exception as e:
    print('An exception was raised')
    print(e.args)
