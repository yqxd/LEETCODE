'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == '':
            return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    now = board[i][j]
                    if self.oneexist(board, word[1:], i, j):
                        return True
                    board[i][j] = now
        return False

    def oneexist(self, board, word, i, j):
        if word == '':
            return True
        else:
            now = board[i][j]
            board[i][j] = ' '
            if j > 0 and board[i][j - 1] == word[0]:
                if self.oneexist(board, word[1:], i, j - 1):
                    return True
            if i > 0 and board[i - 1][j] == word[0]:
                if self.oneexist(board, word[1:], i - 1, j):
                    return True
            if i < len(board) - 1 and board[i + 1][j] == word[0]:
                if self.oneexist(board, word[1:], i + 1, j):
                    return True
            if j < len(board[0]) - 1 and board[i][j + 1] == word[0]:
                if self.oneexist(board, word[1:], i, j + 1):
                    return True
            board[i][j] = now
            return False


A = Solution()

board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]

print(A.exist(board, 'AAB'))
