#Leetcode url - https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = 0
        head = ListNode(0)
        cur = head

        count = 1
        while l1 is not None:
            out = l1.val*count + out
            l1 = l1.next
            count *= 10
        print(out)
        count = 1
        while l2 is not None:
            out = l2.val*count + out
            l2 = l2.next
            count *= 10
        print(out)
        if out == 0:
            return head
        while out > 0:
            cur.next = ListNode(out%10)
            out = out//10 #uses built-in floor function!!!!
            cur = cur.next
        return head.next

a = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
b = [5,6,4]
test1 = ListNode(0)
cur = test1
for num in a:
    cur.next = ListNode(num)
    cur = cur.next

test2 = ListNode(0)
cur = test2
for num in b:
    cur.next = ListNode(num)
    cur = cur.next

c = Solution()
d = c.addTwoNumbers(test1.next, test2.next)
