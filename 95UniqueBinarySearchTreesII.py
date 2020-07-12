'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


Constraints:

0 <= n <= 8
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate_trees(start, end):

            if (start > end):
                return [None, ]

            ans = []
            for i in range(start, end + 1):  # pickup i as root

                left_trees = generate_trees(start, i - 1)  # all possible left subtrees, if i is chosen as root
                right_trees = generate_trees(i + 1, end)  # all possible right subtrees, if i is chosen as root
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)  # root
                        curr_tree.left = l
                        curr_tree.right = r
                        ans.append(curr_tree)
            return ans

        return generate_trees(1, n) if n else []

A = Solution()
print(A.generateTrees(3))