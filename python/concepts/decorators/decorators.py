# adapted from
# https://realpython.com/blog/python/primer-on-python-decorators/
# and a conversation with github.com/zancas

from decorators_mod import mod_outer

def section(msg):
    print("\n-- " + str(msg) + " --\n")


section('First class objects')


def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))

section('Nested functions')


def parent():
    print("Printing from the parent function")

    def first_child():
        return "Printing from the first child."

    def second_child():
        return "Printing from the second child."

    print(first_child())
    print(second_child())

parent()

section("Returning functions")


def parent_rf(num):

    def child_1():
        return "This is what is returned from child_1."

    def child_2():
        return "This is what is returned from child_2."

    try:
        assert num == 10
        return child_1
    except:
        return child_2


foo_rf = parent_rf(10)
bar_rf = parent_rf(11)

print(foo_rf)
print(bar_rf)

print(foo_rf())
print(bar_rf())

section("Decorators")


def outer_function(inner_function):

    def wrapper():
        print("before...")
        inner_function()
        print("after...")

    return wrapper


def just_some_function():
    print("Just some function.")

print ("before just_some_function is assigned, lets try to call it")

just_some_function()

# no before, no after, and no error

just_some_function = outer_function(just_some_function)

just_some_function()

section("decorator 2")


def outer_function2(inner_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes.")
        else:
            print("No.")

        inner_function()

        print("After inner_function() is called.")

    return wrapper

def just_some_function2():
    print ("just_some_function2")

just_some_function2 = outer_function2(just_some_function2)

just_some_function2()

section("Using an import and standard @ syntax")

@mod_outer
def another_function():
    print("Another Function")

another_function()
