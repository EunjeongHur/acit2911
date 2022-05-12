import pytest

from credit import Credit


def test_credit():
    term = "Term 2"
    credit = Credit(term)
    assert credit.term == "Term 2"
    
def test_credit_erros():
    with pytest.raises(KeyError):
        term = "abcd"
        Credit(term)

def test_find_course():
    credit = Credit("Term 1")
    assert 4.0 == credit.find_course("ACIT 1420 - Introduction to Systems Administration")
    assert 3.0 == credit.find_course("ORGB 1100 - Organizational Behaviour")
    assert None == credit.find_course("abcd")
    assert None == credit.find_course("acit2520")
    
