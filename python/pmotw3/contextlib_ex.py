"""
Examples from, adaptations of, and responses to:
https://pymotw.com/3/contextlib/index.html#module-contextlib
"""

import contextlib

tidy = []

with open('/tmp/pmotw.txt', 'wt') as f:
    f.write('Contents go here.')


class Context:

    def __init__(self):
        print('Context.__init__')

    def __enter__(self):
        print('Context.__enter__()')
        return self  # The object returned here is associated with the `as`... 

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context.__exit()__')
        tidy.append('Context')


with Context():
    print('Doing work in the context.')


class ExampleObject:

    def __init__(self, context):
        print('__init__ of Example Object within {}'.format(context))

    def do_all_the_things(self):
        print('ExampleObject.do_all_the_things()')

    def __del__(self):
        tidy.append('ExampleObject.__del__')

class ContextTwo:

    def __init__(self):
        print('ContextTwo.__init__()')

    def __enter__(self):
        print('ContextTwo.__enter__()')
        return ExampleObject(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('ContextTwo.__exit__()')
        tidy.append('ContextTwo')

with ContextTwo() as c:
    c.do_all_the_things()


class ContextThree:

    def __init__(self, handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print('ContextThree.__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('ContextThree.__exit__()')
        print('ext_type =', exc_type)
        print('exc_val  =', exc_val)
        print('exc_tb   =', exc_tb)
        tidy.append('ContextThree')
        return self.handle_error

with ContextThree(True):
    raise RuntimeError('error msg when handled')

print()

# with ContextThree(False):
#     raise RuntimeError('Error msg when not handled')



class AsDecorator(contextlib.ContextDecorator):

    def __init__(self, how_used):
        self.how_used = how_used
        print('AsDecorator.__init__({})'.format(how_used))

    def __enter__(self):
        print('AsDecorator.__enter__({})'.format(self.how_used))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('AsDecorator.__exit__({})'.format(self.how_used))
        tidy.append('AsDecorator.{}'.format(self.how_used))

print('\n--- As Decorator part 0 ---\n')

with AsDecorator('As context manager.'):
    print('Doing all the things after invoked from `with`.')

print('\n--- As Decorator part 1 ---\n')

@AsDecorator('As a decorator.')
def func(msg):
    print(msg)

print() 
func('Doing all the things after invoked as a _function_!')


print('\n--- The context manager decorater ---')


@contextlib.contextmanager
def make_context():
    print('  entering')
    try:
        yield {}  # TODO: This is not explained, research further.
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')

print('Normal:')
with make_context() as value:
    print('  inside with statement:', value)

print('\nHandled Error:')
with make_context() as value:
    raise RuntimeError('error example')

@make_context()
def compact_example(msg, err=None):
    print(msg)
    if err:
        raise err
    else:
        print('Decorated, rather than invoked using `with`.')

compact_example('Normal example.')

compact_example('\nHandled Error', RuntimeError('This error was raised and handled ...'))

print('\n--- Handle Demo ---\n')

class Door:

    def __init__(self):
        print('  door.__init__')
        self.open = True
    
    def close(self):
        print('  door.close()')
        self.open = False

with contextlib.closing(Door()) as door:
    print('  inside with; Is the door open? {}'.format(door.open))
print('  After with; Is the door open? {}'.format(door.open))

print('\nAnd if an error occurs...')
try:
    with contextlib.closing(Door()) as door:
        print('  inside with; Is the door open? {}'.format(door.open))
        raise ValueError('Ran into an error while the door was open.')
except ValueError as err:
    print('  Handled ERROR:', err)

print('  After with; Is the door open? {}'.format(door.open))

print('--- Non Fatal Error ---')

class LibraryError(Exception):
    """Error raised by library that can be ignored (as example)."""
    pass

def code_using_library():
    """In this imagined scenario, the error is intermittent and can always be ignored."""
    raise LibraryError('The operation failed because of existing state.')

with contextlib.suppress(LibraryError):
    print('Attempting operation that, in this case, will raise the "intermittent" error.')
    code_using_library()
    print('Error suppressed. In reality, we almost certainly want to log this error?')

print('Context completed.')


# Some housekeeping, to keep the GC from interleaving __exit__ calls...
print('\n--- TIDY ---\n')
for result in tidy:
    print(result)

