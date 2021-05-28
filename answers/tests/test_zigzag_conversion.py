import unittest
from zigzag_conversion import *


class Test(unittest.TestCase):
    def test_two_sum(self):
        solution = Solution()
        self.assertEqual("PAHNAPLSIIGYIR", solution.convert("PAYPALISHIRING", 3))
        self.assertEqual("PINALSIGYAHRPI", solution.convert("PAYPALISHIRING", 4))
        self.assertEqual("PHASIYIRPLIGAN", solution.convert("PAYPALISHIRING", 5))
        self.assertEqual("ABCD", solution.convert("ABCD", 4))
        self.assertEqual("AB,.CDE", solution.convert("AB,.CDE", 7))
        self.assertEqual("ACB.D,E", solution.convert("AB,.CDE", 3))
        self.assertEqual("A", solution.convert("A", 1))
        self.assertEqual("AB", solution.convert("AB", 1))


if __name__ == '__main__':
    unittest.main()
