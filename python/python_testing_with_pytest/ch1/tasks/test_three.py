"""Test the Task data type."""

import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


@pytest.mark.foo
def test_defaults():
    """Using no params should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


@pytest.mark.baz
def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'Anon')
    assert t.summary == 'buy milk'
    assert t.owner == 'Anon'
    assert (t.done, t.id) == (False, None)
