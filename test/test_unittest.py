import sys
import os
import unittest
from src import calculator

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(5, 0), 5)
        
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(5, 0), 5)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.divide(6,2),3)
        self.assertEqual(calculator.divide(-1,-1), 1)
        self.assertEqual(calculator.divide(-1,100),-0.01)


if __name__ == '__main__':
    unittest.main()