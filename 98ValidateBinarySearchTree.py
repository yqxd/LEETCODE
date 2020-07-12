'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isVone(root, -float('Inf'), float('Inf'))

    def isVone(self, root, l, u):
        if root == None:
            return True
        else:
            return self.isVone(root.left, l, root.val) and self.isVone(root.right, root.val, u) and (
                        root.left == None or (root.left.val < root.val and root.left.val > l)) and (
                               root.right == None or (root.right.val > root.val and root.right.val < u))
