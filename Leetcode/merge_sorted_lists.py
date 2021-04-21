#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        return head.next

test1 = ListNode(1)
test2 = [ListNode(a) for a in range(1,10,3)]
a = Solution()
a.mergeTwoLists()
