'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            now = head
            num = now.val
            while True:
                if now == None:
                    return head
                elif now.next == None:
                    return head
                elif now.next.val != num:
                    now = now.next
                    num = now.val
                else:
                    before = now
                    while now != None and now.val == num:
                        now = now.next
                    before.next = now
                    if now == None:
                        return head
                    else:
                        num = now.val


a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)

a.next = b
b.next = c
c.next = None
d.next = e

A = Solution()
a = A.deleteDuplicates(a)

while a != None:
    print(a.val)
    a = a.next
