from test import add,sub,mul,div
from test import calcc
import pytest
# def test_add():
#     res=add(2,3)
#     assert res==5 
# def test_sub():
#     res=sub(2,3)
#     assert res==-1
# def test_mul():
#     res=mul(2,3)
#     assert res==6
# def test_div():
#     res=div(10,5)
#     assert res==2
# def test_calc():
#     assert add(1,2)==3
#     assert sub(9,2)==7
#     assert mul(1,2)==2
#     assert div(10,2)==5
@pytest.fixture
def calc():
     return calcc()
def test_calc_add(calc):
    assert calc.add(1,2)==3
@pytest.mark.parametrize("num1,num2,expected",[(2,3,5),(3,4,7)])
def test_calc_add_param(calc,num1,num2,expected):
    assert calc.add(num1,num2)==expected    

def test_divide_by_zero():
    with pytest.raises(ValueError):
        div(10,0)