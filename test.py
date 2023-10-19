import pytest
from main import Calculator

def test_add():
    calc = Calculator()
    res = calc.add(2,3) 
    assert res == 5

def test_substract():
    calc = Calculator()
    res = calc.substract(2,3) 
    assert res == -1

def test_multiplication():
    calc = Calculator()
    res = calc.multiplication(2,3) 
    assert res == 6

def test_division():
    calc = Calculator()
    res = calc.division(5,4) 
    assert res == 1.25

def test_integral_division():
    calc = Calculator()
    res = calc.integral_division(5, 4) 
    assert res == 1

def test_remainder():
    calc = Calculator()
    res = calc.remainder(15, 4)
    assert res == 3