"""
This module is a sandbox and example of patterns for class instance
initiation and also an exploration of static methods.
"""

def function():
    return "function()"

class Example(object):
    
    def __init__(self, arg):
        self.arg = arg
        self.foo = "instance.foo"
        self.bar = function()              # Confusing, do not do this.
        self._init_helper_method()
        self.qux = Example.static_method() # Do this instead.

    def method(self):
        return "instance.method()"
    
    @staticmethod
    def static_method():
        return "instance.static_method()"

    def _init_helper_method(self):
        self.baz = "instance." + self.arg

instance = Example("baz")
print(vars(instance))

print(function())
print(instance.foo)
print(instance.method())
print(instance.baz)
print(instance.static_method())

