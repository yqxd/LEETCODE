'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = {}
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m+1):
            d[(i, 0)] = float('Inf')
        for j in range(1, n+1):
            d[(0, j)] = float('Inf')
        d[(0, 1)] = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                d[(i, j)] = grid[i-1][j-1] + min(d[(i-1, j)], d[(i, j-1)])
        return d[(m, n)]

A = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(A.minPathSum(grid))