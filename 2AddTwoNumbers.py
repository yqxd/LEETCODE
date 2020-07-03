'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        x1 = ListNode(0)
        x = x1
        while l1 or l2:
            if l1:
                x.val += l1.val
                l1 = l1.next
            if l2:
                x.val += l2.val
                l2 = l2.next
            x.val = x.val + add
            add = 0
            if x.val >= 10:
                x.val = x.val - 10
                add = 1
            if add == 1 or l1 or l2:
                x.next = ListNode(0)
                x = x.next
        if add == 1:
            x.val += 1
        return x1