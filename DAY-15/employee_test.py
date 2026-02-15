import pytest
from employee import Employee
@pytest.fixture
def employee():
    return Employee(1,"sowmya",1000)
@pytest.mark.parametrize("num1,expected",[(2000,3000),(1000,2000)])
def test_increase_salary(employee,num1,expected):
    assert employee.increase_salary(num1)==expected
@pytest.mark.parametrize("num1,expected",[(200,800),(100,900)])
def test_decrease_salary(employee,num1,expected):
    assert employee.decrease_salary(num1)==expected
    
