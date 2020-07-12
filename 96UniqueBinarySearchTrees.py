'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = {}
        d[0] = 1
        d[1] = 1
        for i in range(2, n + 1):
            d[i] = sum(d[j] * d[i - 1 - j] for j in range(i))
        return d[n]


A = Solution()
print(A.numTrees(3))
