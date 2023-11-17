from answers.common.list_node import ListNode


def array_to_linked_list(array):
    head = None
    tail = None

    for i in array:
        current = ListNode(i)
        if head is None:
            head = current
        else:
            tail.next = current

        tail = current

    return head


def compare_linked_list(l1, l2):
    p_l1 = l1
    p_l2 = l2

    while p_l1 is not None and p_l2 is not None:
        if p_l1.val != p_l2.val:
            break
        p_l1 = p_l1.next
        p_l2 = p_l2.next

    return True if p_l1 is None and p_l2 is None else False


