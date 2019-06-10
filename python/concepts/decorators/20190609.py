# More thoughts on decorators

def decorator(func_to_be_decorated):
    def decorating_function():
        print(func_to_be_decorated.__name__)
        return func_to_be_decorated()
    return decorating_function


# Explicit
def spec_func_to_dec():
    print('The core functionality')

decorated = decorator(spec_func_to_dec)
decorated()

# Simplified (syntactic sugar)
@decorator
def alt_func_to_dec():
    print('The alternative core functionality')

alt_func_to_dec()


def parameterized_dec(func_to_be_decorated):
    def decorating_function(*args, **kwargs):
        print(args, kwargs)
        return func_to_be_decorated(*args, **kwargs)
    return decorating_function


@parameterized_dec
def example_func_args_and_kwargs(arg0, arg1, foo="", bar=""):
    print('And now we would do all the things with the args and kwargs')

example_func_args_and_kwargs("foo", "bar", foo="baz", bar="qux")
