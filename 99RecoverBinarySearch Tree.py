'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.swap1, self.swap2, self.inter = None, None, None
        self.helper(root)
        self.swap1.val, self.swap2.val = self.swap2.val, self.swap1.val
        return

    def helper(self, node):
        if not node: return

        self.helper(node.left)

        if self.inter and node.val < self.inter.val:
            self.swap1 = node
            if not self.swap2:
                self.swap2 = self.inter
            else:
                return

        self.inter = node
        self.helper(node.right)
        return
        