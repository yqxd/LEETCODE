'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = 1
        k = head
        while k.next != None:
            num += 1
            k = k.next
        if num == n:
            return head.next
        elif num == 1:
            k.next = None
            return head
        else:
            k = head
            for i in range(num - n - 1):
                k = k.next
            k.next = k.next.next
        return head


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
print(A.removeNthFromEnd(a, 2))
