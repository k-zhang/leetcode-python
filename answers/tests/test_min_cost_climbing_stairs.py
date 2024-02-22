from unittest import TestCase

from min_cost_climbing_stairs import min_cost_climbing_stairs


class Test(TestCase):
    def test_min_cost_climbing_stairs(self):
        self.assertEqual(15, min_cost_climbing_stairs([10, 15, 20]))
        self.assertEqual(6, min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
        self.assertEqual(1, min_cost_climbing_stairs([1, 2]))
        self.assertEqual(0, min_cost_climbing_stairs([0, 0, 0, 0]))
        self.assertEqual(0, min_cost_climbing_stairs([0, 0, 0, 1]))
        self.assertEqual(0, min_cost_climbing_stairs([1]))
        self.assertEqual(0, min_cost_climbing_stairs([]))
