import pytest

from pytest import fixture

@fixture
def simple_fixture():
    """
    Fixtures are callables that can be provided in
    any test function as parameters
    They are decorated as @fixture
    """
    print('|fixture is working!')


def test_with_simple_fixture(simple_fixture):
    """
    They can be invoked simply by having a positional arg
    """

    print('Running a simple test with a simple fixture..')
    assert True
