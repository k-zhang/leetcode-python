from unittest import TestCase

from reshape_the_matrix import reshape_the_matrix


class Test(TestCase):
    def test_reshape_the_matrix(self):
        self.assertEqual([[1, 2, 3, 4]], reshape_the_matrix([[1, 2], [3, 4]], 1, 4))
        self.assertEqual([[1, 2], [3, 4]], reshape_the_matrix([[1, 2], [3, 4]], 2, 4))
        self.assertEqual([[1, 2], [3, 4], [5, 6], [7, 8]], reshape_the_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], 4, 2))
        self.assertEqual([[1], [2], [3], [4], [5], [6], [7], [8]],
                         reshape_the_matrix([[1, 2, 3, 4], [5, 6, 7, 8]], 8, 1))
        self.assertEqual([[1]], reshape_the_matrix([[1]], 1, 1))
