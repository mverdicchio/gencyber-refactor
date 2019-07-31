import unittest
import DateCalculator2


class MyTests(unittest.TestCase):
    # every 4 years
    def test1(self):
        return self.assertTrue(DateCalculator2.is_leap_year(2004))

    # but not century years
    def test2(self):
        return self.assertFalse(DateCalculator2.is_leap_year(2004))

    # except 400th century years
    def test3(self):
        return self.assertTrue(DateCalculator2.is_leap_year(2004))

