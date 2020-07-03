'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        now = head
        n = 0
        while now:
            n += 1
            end = now
            now = now.next
        end.next = head
        k = k % n
        now = head
        for i in range(n - k - 1):
            now = now.next
        result = now.next
        now.next = None
        return result


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d

A = Solution()
result = A.rotateRight(head, 5)
while result:
    print(result.val)
    result = result.next
