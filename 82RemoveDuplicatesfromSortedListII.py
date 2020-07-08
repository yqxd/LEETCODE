'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''


# Definition
# for singly - linked list.
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
            before = None
            now = head
            while True:
                if now == None or now.next == None:
                    return head
                elif now.next.val == now.val:
                    num = now.val
                    now = now.next.next
                    while now != None and now.val == num:
                        now = now.next
                    if before != None:
                        before.next = now
                    else:
                        head = now
                else:
                    before = now
                    now = now.next


A = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)
e = ListNode(3)

a.next = b
b.next = c
c.next = d
d.next = e

a = A.deleteDuplicates(a)
while a != None:
    print(a.val)
    a = a.next
