import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98


def test_fun5():
    assert calculator.fun5(6, 2) == 3.0
    assert calculator.fun5(10, 4) == 2.5
    assert calculator.fun5(-4, 2) == -2.0
    assert calculator.fun5(0, 5) == 0.0


def test_fun5_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.fun5(1, 0)


def test_fun5_invalid_input():
    with pytest.raises(ValueError, match="Both inputs must be numbers"):
        calculator.fun5("1", 2)
    with pytest.raises(ValueError, match="Both inputs must be numbers"):
        calculator.fun5(1, None)


def test_fun6():
    assert calculator.fun6(2, 3) == 8
    assert calculator.fun6(5, 0) == 1
    assert calculator.fun6(-2, 2) == 4
    assert calculator.fun6(10, 2) == 100


def test_fun6_invalid_input():
    with pytest.raises(ValueError, match="Both inputs must be numbers"):
        calculator.fun6(2, "3")


def test_fun7():
    assert calculator.fun7(7, 3) == 1
    assert calculator.fun7(10, 5) == 0
    assert calculator.fun7(-5, 3) == 1
    assert calculator.fun7(0, 7) == 0


def test_fun7_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot take modulo by zero"):
        calculator.fun7(5, 0)


def test_fun7_invalid_input():
    with pytest.raises(ValueError, match="Both inputs must be numbers"):
        calculator.fun7(10, "2")

