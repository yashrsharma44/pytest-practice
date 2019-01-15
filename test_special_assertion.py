import pytest

def test_division_by_zero():
    """
    This function demonstrates the different type of
    assertion, pytest offers
    """
    a = 5
    b = 0

    with pytest.raises(ZeroDivisionError):
        a / b

def test_keyerror_details():
    """
    The Raised exception can be used 
    for further exception
    """

    my_map = {'foo':'bar'}

    with pytest.raises(KeyError) as e:
        assert my_map['bar']
    
    print('Raised Error :{}'.format(e.value))

def test_approx_matches():
    """
    This function applies approximate assertion
    on functions returning approx values
    """
    assert (0.1 + 0.2) == pytest.approx(0.3)

