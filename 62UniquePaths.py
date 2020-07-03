'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = {}
        for i in range(1, m + 1):
            d[(i, 1)] = 1
        for i in range(1, n + 1):
            d[(1, i)] = 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                d[(i, j)] = d[(i - 1, j)] + d[(i, j - 1)]
        return d[(m, n)]


A = Solution()
print(A.uniquePaths(3, 2))
