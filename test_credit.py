import pytest

from credit import Credit


def test_credit():
    term = "term2"
    credit = Credit(term)
    assert credit.term == "term2"
    
def test_credit_erros():
    with pytest.raises(KeyError):
        term = "abcd"
        Credit(term)

def test_find_course():
    credit = Credit("term1")
    assert 4.0 == credit.find_course("acit1420")
    assert 3.0 == credit.find_course("orgb1100")
    assert None == credit.find_course("abcd")
    assert None == credit.find_course("acit2520")
    
