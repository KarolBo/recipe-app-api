"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Calc test case"""

    def test_add_numbers(self):
        """testing add"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Testing subtract"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, -5)
