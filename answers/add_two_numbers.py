class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, ListNode):
            return NotImplemented
        return self.val == o.val and self.next.__eq__(o.next)


class Solution(object):
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = None
        tail = head

        while (l1 is not None) or (l2 is not None) or (carry != 0):
            result = self.calculate(l1, l2, carry)
            if result < 10:
                result_node = ListNode(result)
                carry = 0
            else:
                result_node = ListNode(result % 10)
                carry = result // 10

            if head is None:
                head = result_node
                tail = head
            else:
                tail.next = result_node
                tail = tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return head

    @staticmethod
    def calculate(pl1: ListNode, pl2: ListNode, carry: int) -> int:
        if (pl1 is not None) and (pl2 is not None):
            return pl1.val + pl2.val + carry
        elif pl1 is not None:
            return pl1.val + carry
        elif pl2 is not None:
            return pl2.val + carry
        else:
            return carry
