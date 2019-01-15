import string

from pytest import fixture

@fixture(params=['a','b','c','d','e'])
def letters_fixture(request):
    """
    Fixtures with paramters that will run once per param(via request)
    """
    yield request.param

def test_paramterization(letters_fixture):

    assert letters_fixture in string.ascii_letters
