from answers.common.list_node import ListNode


def merge_two_sorted_list(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    pre_head = ListNode(-1)
    p = pre_head

    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next

        p = p.next

    p.next = l2 if l1 is None else l1

    return pre_head.next
