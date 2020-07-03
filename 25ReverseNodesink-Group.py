'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        now = head
        lists = [head]
        while now.next != None:
            now = now.next
            lists += [now]
        n = len(lists)
        lists[0:k] = self.reverseOne(lists[0:k], k)
        now = k
        for i in range(n // k - 1):
            lists[now:(now + k)] = self.reverseOne(lists[now:(now + k)], k)
            lists[now - 1].next = lists[now]
            now += k
        if now < len(lists):
            lists[now - 1].next = lists[now]
        else:
            lists[now - 1].next = None
        return lists[0]

    def reverseOne(self, lists, k):
        """
        :type lists: List[ListNode]
        :type k: int
        """
        for i in range(k - 1):
            lists[k - 1 - i].next = lists[k - 2 - i]
        lists.reverse()
        return lists


A = Solution()

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

t = A.reverseKGroup(a1, 2)
while t.next != None:
    print(t.val)
    t = t.next
print(t.val)
