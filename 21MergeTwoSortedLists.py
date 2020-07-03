'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val > l2.val:
            l1,l2 = l2,l1
        head = l1
        l1 = l1.next
        now = head
        while True:
            if l1 == None:
                now.next = l2
                break
            elif l2 == None:
                now.next = l1
                break
            else:
                if l1.val <= l2.val:
                    now.next = l1
                    l1 = l1.next
                else:
                    now.next = l2
                    l2 = l2.next
                now = now.next
        return head


A = Solution()

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(4)
l3.next = l2

s1 = ListNode(1)
s2 = ListNode(3)
s1.next = s2
s3 = ListNode(4)
s3.next = s2

A.mergeTwoLists(l1, s1)