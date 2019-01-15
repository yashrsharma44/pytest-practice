import pytest

@pytest.mark.parametrize("number",[1,2,3,4,5])
def test_numbers(number):
    """
    This function asserts the power function
    using marked paramterized without using a fixture
    """
    assert number ** 2 == number ** 2


@pytest.mark.parametrize('x, y',[(1,2),(2,1)])
def test_cube(x,y):

    assert x ** 3 == x ** 3



