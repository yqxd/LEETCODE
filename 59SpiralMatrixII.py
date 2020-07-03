'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[-1 for j in range(n)] for i in range(n)]
        d = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        now = [0, 0]
        k = 0
        for i in range(1, 1 + n * n):
            A[now[0]][now[1]] = i
            if self.check(A, n, now[0] + d[k][0], now[1] + d[k][1]):
                now[0] += d[k][0]
                now[1] += d[k][1]
            else:
                k = (k + 1) % 4
                now[0] += d[k][0]
                now[1] += d[k][1]
        return A

    def check(self, A, n, i, j):
        if i == n or j == n or i == -1 or j == -1:
            return False
        elif A[i][j] != -1:
            return False
        return True


A = Solution()
print(A.generateMatrix(3))
