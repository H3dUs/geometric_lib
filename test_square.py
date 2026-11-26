import unittest

import square


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_square_mul(self):
        self.assertEqual(square.area(10), 100)

    def test_float_side(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_integer_side(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_float_side(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10)