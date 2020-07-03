'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = {}
        for i in range(m+1):
            d[(i, 0)] = 0
        for j in range(n+1):
            d[(0, j)] = 0
        if obstacleGrid[0][0] == 0:
            d[(0, 0)] = 0
            d[(0, 1)] = 1
        else:
            return 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1]:
                    d[(i, j)] = 0
                else:
                    d[(i, j)] = d[(i, j-1)] + d[(i-1, j)]
        return d[(m, n)]

A = Solution()
print(A.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))