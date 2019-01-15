from pytest import fixture

@fixture(params=['a','b','c','d'])
def letters_fixture(request):
    """
    Fixtures can cause tests to be run multiple times
    (once per parameter)
    """

    yield request.param

@fixture(params=[1,2,3,4])
def numbers_fixture(request, letters_fixture):
    """
    Fixtures can invoke each other , producing cartesian product
    """
    yield request.param

def test_fixtureception(numbers_fixture, letters_fixture):

    print('\n 11 {} 11'.format(str(numbers_fixture)+letters_fixture))
