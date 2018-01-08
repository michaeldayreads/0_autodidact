#import pytest
import inspect

def whoamiinside():
    f = inspect.stack()[2][0]
    return inspect.getframeinfo(f)[3][0].strip()


def a_contrast():
    print("foo qux")
    print(whoamiinside())

a_contrast()

@pytest.fixture(scope='session', autouse=True)
def mytest_fixture():
    print("fixture 1")

def test_1():
    print("in test_1")
    print(whoamiinside())

def test_2():
    print("in test_2")

@pytest.fixture(scope='session', autouse=False)
def mytest_fixture_2():
    print("fixture 2")

def test_3():
    print("in test_3")

def test_4():
    print("in test_4")