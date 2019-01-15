from pytest import fixture

@fixture
def yield_fixture():
    """
    Fixtures can yield data - additional code can be run after the test
    Can be used as a setUp and tearDown method

    Note : You cannot add a second yield statement
    """
    x = {'foo':'bar'}

    yield x

    x = None

def test_with_yield_fixture(yield_fixture):
    
    assert 'foo' in yield_fixture
