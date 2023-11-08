import unittest
from zigzag_conversion import *


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual("PAHNAPLSIIGYIR", convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", convert("PAYPALISHIRING", 4))
        self.assertEqual("PHASIYIRPLIGAN", convert("PAYPALISHIRING", 5))
        self.assertEqual("ABCD", convert("ABCD", 4))
        self.assertEqual("AB,.CDE", convert("AB,.CDE", 7))
        self.assertEqual("ACB.D,E", convert("AB,.CDE", 3))
        self.assertEqual("A", convert("A", 1))
        self.assertEqual("AB", convert("AB", 1))


if __name__ == '__main__':
    unittest.main()
