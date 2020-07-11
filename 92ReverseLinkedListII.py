'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        start = curr = dummy
        next = curr.next

        for _ in range(m - 1):
            start = curr = next
            next = curr.next

        for _ in range(n - m + 1):
            prev = curr
            curr = next
            next = curr.next
            curr.next = prev

        start.next.next = next
        start.next = curr

        return dummy.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
A = Solution()
print(A.reverseBetween(a, 1, 4))
s = d
while s != None:
    print(s.val)
    s = s.next
