import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator


class TestCalculator(unittest.TestCase):

    def test_fun1(self):
        self.assertEqual(calculator.fun1(2, 3), 5)
        self.assertEqual(calculator.fun1(5, 0), 5)
        
        self.assertEqual(calculator.fun1(-1, 1), 0)
        self.assertEqual(calculator.fun1(-1, -1), -2)

    def test_fun2(self):
        self.assertEqual(calculator.fun2(2, 3), -1)
        self.assertEqual(calculator.fun2(5, 0), 5)
        self.assertEqual(calculator.fun2(-1, 1), -2)
        self.assertEqual(calculator.fun2(-1, -1), 0)

    def test_fun3(self):
        self.assertEqual(calculator.fun3(2, 3), 6)
        self.assertEqual(calculator.fun3(5, 0), 0)
        self.assertEqual(calculator.fun3(-1, 1), -1)
        self.assertEqual(calculator.fun3(-1, -1), 1)

    def test_fun4(self):
        self.assertEqual(calculator.fun4(2, 3, 5), 10)
        self.assertEqual(calculator.fun4(5, 0, -1), 4)
        self.assertEqual(calculator.fun4(-1, -1, -1), -3)
        self.assertEqual(calculator.fun4(-1, -1, 100), 98)

    def test_fun5(self):
        self.assertEqual(calculator.fun5(6, 2), 3.0)
        self.assertEqual(calculator.fun5(10, 4), 2.5)
        self.assertEqual(calculator.fun5(-4, 2), -2.0)
        self.assertEqual(calculator.fun5(0, 5), 0.0)

    def test_fun5_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            calculator.fun5(1, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_fun5_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.fun5("1", 2)
        with self.assertRaises(ValueError):
            calculator.fun5(1, None)

    def test_fun6(self):
        self.assertEqual(calculator.fun6(2, 3), 8)
        self.assertEqual(calculator.fun6(5, 0), 1)
        self.assertEqual(calculator.fun6(-2, 2), 4)
        self.assertEqual(calculator.fun6(10, 2), 100)

    def test_fun6_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.fun6(2, "3")

    def test_fun7(self):
        self.assertEqual(calculator.fun7(7, 3), 1)
        self.assertEqual(calculator.fun7(10, 5), 0)
        self.assertEqual(calculator.fun7(-5, 3), 1)
        self.assertEqual(calculator.fun7(0, 7), 0)

    def test_fun7_modulo_by_zero(self):
        with self.assertRaises(ValueError) as context:
            calculator.fun7(5, 0)
        self.assertIn("Cannot take modulo by zero", str(context.exception))

    def test_fun7_invalid_input(self):
        with self.assertRaises(ValueError):
            calculator.fun7(10, "2")


if __name__ == '__main__':
    unittest.main()