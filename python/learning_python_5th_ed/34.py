# # basic example
#
# def gobad(x, y):
#     return x / y
#
# def gosouth(x):
#     print(gobad(x, 0))
#
# gosouth(1)


# # built in examples
#
# def kaboom(x, y):
#     print(x +y)
#
# try:
#     kaboom([0, 1, 2], 'spam')
# except TypeError:
#     print('TypeError! D\'oh!')
# print('resumeing, regardless of exception')

# # testing bare except
#
# def kaboom(x, y):
#     print(x +y)
#
# try:
#     nonexistent_function()
#     kaboom([0, 1, 2], 'spam')
# except:
#     print('Bare except. Bad idea...')
# print('resumeing, regardless of exception')

# # unified example
#
# sep = '-' * 45 + '\n'
#
# print(sep + 'Exception raised & caught')
#
# try:
#     x = 'spam'[99]
# except IndexError:
#     print('Except ran')
# finally:
#     print('finally ran')
#
# print('after ran')
#
# print(sep + 'No exception raised')
#
# try:
#     x = 'spam'[3]
# except IndexError:
#     print('except ran')
# finally:
#     print('finally ran')
#
# print('after ran')
#
# print(sep + 'exception raised, but not caught')
#
# try:
#     x = 1 / 0
# except IndexError:
#     print('except ran')
# finally:
#     print('finally ran')
#
# print('after ran')

# # scope in except
#
# try:
#     1 / 0
# except Exception as X:
#     print('in the exception: %s', X)
#
# print('And outside of the try block: %s', X)
#
# # in p2, we see the message both times
# # in p3, we get a name error on the second print.
#
# # compare to

# # comprehension example
# X = 99
# {X for X in 'spam'}
# print(X)

# try:
#     1 / 0
# except Exception as X:
#     print(X)
#     Saveit = X
#
# print(Saveit)
# print(X)
#
# # p2 -> three instances of same message, division or modulo by 0
# # p3 -> two 'division by zero' then a traceback to a NameError

# # exception chaining
# # p3 only, p2 shows only the last error in the stacktrace
#
# try:
#     try:
#         1 / 0
#     except:
#         badname
# except:
#     open('yetanotherbadname')

# with/as context managers - an alternative to try/finally
# useful for clean up
# less general than try/finally where
#
# with expression as variable:
#    with block ...
#
# is expecting the expression to return an object that supports context management protocol
#
# Supporting that protocal means there is a __enter__ and __exit__ method on the class.
# The value returned by the __enter__ method is what is assigned to the varaible from the as above.
#

class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1, no error')
        print('we get here...')

    with TraceBlock() as action:
        action.message('test 2, error!')
        raise TypeError
        print('but not here...')
