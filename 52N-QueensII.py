'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = self.findone([], n, n)
        return len(result)

    def findone(self, lists, k, n):
        if k == 0:
            return [lists]
        else:
            result = []
            for i in range(n):
                if self.check(lists, i):
                    result += self.findone(lists + [i], k - 1, n)
            return result

    def check(self, lists, i):
        if i in lists:
            return False
        for j in range(len(lists)):
            if abs(len(lists) - j) == abs(i - lists[j]):
                return False
        return True

    def conv(self, l, n):
        result = []
        for i in range(n):
            result += ['']
            for j in range(n):
                if l[i] == j:
                    result[i] += 'Q'
                else:
                    result[i] += '.'
        return result


A = Solution()
print(A.totalNQueens(4))
