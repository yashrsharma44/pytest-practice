from pytest import fixture

@fixture
def one_fixture():
    """
    pytest fixtures can also return values,
    when passed as a parameter
    """

    return 1

def test_with_data_fixture(one_fixture):
    """
    uses the fixture values to perform assertion
    """

    assert one_fixture == 1
