from src import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(5,0) == 5
    assert calculator.add (-1, 1) == 0
    assert calculator.add (-1, -1) == -2


def test_fun2():
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(5,0) == 5
    assert calculator.subtract (-1, 1) == -2
    assert calculator.subtract (-1, -1) == 0

def test_fun3():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(5,0) == 0
    assert calculator.multiply (-1, 1) == -1
    assert calculator.multiply (-1, -1) == 1

def test_fun4():
    assert calculator.divide(6,2) == 3
    assert calculator.divide(0,5) == 0
    assert calculator.divide (-1, -1) == 1
    assert calculator.divide (-1, 100) == -0.01