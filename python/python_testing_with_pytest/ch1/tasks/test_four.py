"""Test the Task data type."""

import pytest
from collections import namedtuple


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


@pytest.mark.baz
def test_asdict():
    """_asdict() should return a dictionary."""
    t_task = Task('thing to do', 'Anon', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'thing to do',
        'owner': 'Anon',
        'done': True,
        'id': 21}
    assert t_dict == expected


@pytest.mark.foo
def test_replace():
    """replace() should change passed in fields."""
    t_before = Task('finish book', 'Anon', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'Anon', True, 10)
    assert t_after == t_expected
