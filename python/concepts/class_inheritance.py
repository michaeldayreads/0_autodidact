class Base(object):
    def __init__(self, foo, bar):
        self.foo=foo
        self.bar=bar

class Sub(Base):
    """Verbose version."""
    def __init__(self, qux, foo, bar):
        super().__init__(foo, bar)
        self.qux = qux


class Alt_sub(Base):
    """Abreviated version. Useful when there are lots of args."""
    def __init__(self, qux, *args):
        super().__init__(*args)
        self.qux = qux


my_base = Base("Foo", "Bar")
print(my_base.__dict__)

my_sub = Sub("qux", "foo", "bar")
print(my_sub.__dict__)

my_alt = Alt_sub("ALT", "foo", "bar")
print(my_alt.__dict__)
