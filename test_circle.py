import math
import unittest

import circle


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(circle.area(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_integer_radius(self):
        self.assertAlmostEqual(circle.area(3), 9 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(circle.area(0.5), 0.25 * math.pi)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_float_radius(self):
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi)