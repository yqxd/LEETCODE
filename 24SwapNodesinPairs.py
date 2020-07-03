'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            now = head.next
            now1 = now.next
            now.next = head
            head.next = now1
            head = now
            now = now.next
        while True:
            if now.next == None or now.next.next == None:
                return head
            else:
                now1 = now.next
                now2 = now1.next
                now3 = now2.next
                now.next = now2
                now2.next = now1
                now1.next = now3
                now = now2


A = Solution()
head = ListNode(1)
head1 = ListNode(2)
head2 = ListNode(3)
head3 = ListNode(4)
head.next = head1
head1.next = head2
head2.next = head3
print(A.swapPairs(head))
