from pytest import fixture

def risky_function():

    # Function to simulate a failure , a risky affair!
    raise Exception('Whoops! I guess that risky function didn\'t work!')

def safe_cleanup():
    print('CleanUp mode : ON')

@fixture
def safe_fixture(request):
    """
    The request can also be used to aplly post
    -tests callback
    """

    print('\n Starting safe_fixture setup')

    request.addfinalizer(safe_cleanup)

    # risky_function()

    print('Finishing safe fixture setup')


def test_with_safe_cleanup_fixture(safe_fixture):

    assert True