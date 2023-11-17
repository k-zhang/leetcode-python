from unittest import TestCase

from find_the_town_judge import find_the_town_judge


class Test(TestCase):
    def test_find_the_town_judge(self):
        self.assertEqual(1, find_the_town_judge(1, []))
        self.assertEqual(2, find_the_town_judge(2, [(1, 2)]))
        self.assertEqual(3, find_the_town_judge(3, [(1, 3), (2, 3)]))
        self.assertEqual(-1, find_the_town_judge(3, [(1, 3), (2, 3), (3, 1)]))
        self.assertEqual(-1, find_the_town_judge(4, [(1, 4), (2, 4)]))
        self.assertEqual(-1, find_the_town_judge(4, [(1, 4), (2, 4), (3, 2)]))
        self.assertEqual(-1, find_the_town_judge(4, [(1, 4), (2, 4), (1, 2), (3, 2), (4, 2)]))
