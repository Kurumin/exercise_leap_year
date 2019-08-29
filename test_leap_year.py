import unittest
from leap_year import is_bissextile


class TestLeapYear(unittest.TestCase):

    def test_not_bissextile_when_1742(self):
        self.assertEqual(False, is_bissextile(1742))

    def test_not_bissextile_when_1889(self):
        self.assertEqual(False, is_bissextile(1889))

    def test_not_bissextile_when_1742(self):
        self.assertEqual(False, is_bissextile(1742))

    def test_not_bissextile_when_1951(self):
        self.assertEqual(False, is_bissextile(1951))

    def test_not_bissextile_when_2011(self):
        self.assertEqual(False, is_bissextile(2011))

    def test_is_bissextile_when_1600(self):
        self.assertEqual(True, is_bissextile(1600))

    def test_is_bissextile_when_1732(self):
        self.assertEqual(True, is_bissextile(1732))

    def test_is_bissextile_when_1888(self):
        self.assertEqual(True, is_bissextile(1888))

    def test_is_bissextile_when_1944(self):
        self.assertEqual(True, is_bissextile(1944))

    def test_is_bissextile_when_2008(self):
        self.assertEqual(True, is_bissextile(2008))

    def test_is_bissextile_when_2016(self):
        self.assertEqual(True, is_bissextile(2016))

    def test_not_bissextile_when_2017(self):
        self.assertEqual(False, is_bissextile(2017))

    def test_not_bissextile_when_2018(self):
        self.assertEqual(False, is_bissextile(2018))

    def test_not_bissextile_when_2019(self):
        self.assertEqual(False, is_bissextile(2019))

    def test_is_bissextile_when_2020(self):
        self.assertEqual(True, is_bissextile(2020))


if __name__ == '__main__':
    unittest.main()
