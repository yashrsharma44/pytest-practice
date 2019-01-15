from pytest import fixture

def introspective_fixture(request):
    """
    This request fixture allows to intropect the caller or the 'requesting' test
    """

    # request.scope
    # request.node
    # request.module
    assert True
