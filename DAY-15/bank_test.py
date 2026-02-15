import pytest
from bank import bank
@pytest.fixture
def Bank():
    return bank(1000)
def test_deposit(Bank):
    assert Bank.deposit(1000)==2000
def testwithdraw(Bank):
    assert Bank.withdraw(1000)==0
    


