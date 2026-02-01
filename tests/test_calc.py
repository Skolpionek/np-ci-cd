import pytest
from app.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 2) == 4

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5

def test_divide_error():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)