import unittest
from add_two_numbers import *



def to_list_node(number):
    if number == 0:
        return ListNode(0)

    p = None
    tail = p
    while number != 0:
        pop = number % 10
        number = number // 10

        if p is None:
            p = ListNode(pop)
            tail = p
        else:
            tail.next = ListNode(pop)
            tail = tail.next

    return p


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(to_list_node(807), add_two_numbers(to_list_node(342), to_list_node(465)))
        self.assertEqual(to_list_node(0), add_two_numbers(to_list_node(0), to_list_node(0)))
        self.assertEqual(to_list_node(1), add_two_numbers(to_list_node(0), to_list_node(1)))
        self.assertEqual(to_list_node(1357), add_two_numbers(to_list_node(123), to_list_node(1234)))
        self.assertEqual(to_list_node(2998), add_two_numbers(to_list_node(999), to_list_node(1999)))


if __name__ == '__main__':
    unittest.main()
