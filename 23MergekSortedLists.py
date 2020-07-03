'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        a = []
        for i in lists:
            if i != None:
                a = self.mergeOne(a, i)
        if a == []:
            return
        head = a[0]
        if head.next == None:
            del a[0]
        else:
            now = a[0].next
            del a[0]
            a = self.mergeOne(a, now)
        now = head
        while len(a) != 0:
            now.next = a[0]
            now = now.next
            if now.next == None:
                del a[0]
            else:
                del a[0]
                a = self.mergeOne(a, now.next)
        return head

    def mergeOne(self, l, head):
        """
        :type l: List[ListNode]
        :type head: listNode
        """
        if l == []:
            return [head]
        a = 0
        b = len(l) - 1
        while True:
            if b - a < 2:
                if l[a].val <= head.val:
                    a = a + 1
                    if l[b].val <= head.val:
                        a = b + 1
                break
            else:
                if l[(b + a) // 2].val > head.val:
                    b = (b + a) // 2
                elif l[(b + a) // 2].val < head.val:
                    a = (b + a) // 2
                else:
                    a = (b + a) // 2
                    break
        l.insert(a, head)
        return l


A = Solution()

a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(5)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
c1 = ListNode(2)
c2 = ListNode(6)

a1.next = a2
a2.next = a3
b1.next = b2
b2.next = b3
c1.next = c2

if 1 == 0:
    for i in new:
        print(i.val)
k = A.mergeKLists([a1, b1, c1])
if 1 == 1:
    while k.next != None:
        print(k.val)
        k = k.next
    print(k.val)
