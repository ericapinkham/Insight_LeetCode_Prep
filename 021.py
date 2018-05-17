# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    new_list = ListNode(None)
    active_node = new_list
    while l1 or l2:
        if l1 and l2:
            if l1.val <= l2.val:
                active_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                active_node.next = ListNode(l2.val)
                l2 = l2.next
        elif l1:
            active_node.next = ListNode(l1.val)
            l1 = l1.next
        elif l2:
            active_node.next = ListNode(l2.val)
            l2 = l2.next
        active_node = active_node.next
    return new_list.next
