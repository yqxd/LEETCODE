'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smallhead = None
        largehead = None
        nowsmall = None
        nowlarge = None
        now = head
        while now != None:
            if now.val < x:
                if smallhead == None:
                    smallhead = now
                    nowsmall = now
                else:
                    nowsmall.next = now
                    nowsmall = now
            else:
                if largehead == None:
                    largehead = now
                    nowlarge = now
                else:
                    nowlarge.next = now
                    nowlarge = now
            now = now.next
        if nowlarge == None:
            return smallhead
        elif nowsmall == None:
            return largehead
        else:
            nowlarge.next = None
            nowsmall.next = largehead
            return smallhead


a = ListNode(2)
b = ListNode(1)
c = ListNode(2)
d = ListNode(5)
e = ListNode(3)

a.next = b
b.next = None
c.next = d
d.next = e

A = Solution()
a = A.partition(a, 2)
while a != None:
    print(a.val)
    a = a.next



