'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = self.findone([], n, n)
        for i in range(len(result)):
            result[i] = self.conv(result[i], n)
        return result

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
print(A.solveNQueens(8))
