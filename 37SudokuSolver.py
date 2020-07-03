class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        i = 0
        j = 0
        while i < 9:
            while j < 9:
                if board[i][j] != '.':
                    j += 1
                else:
                    break
            if j < 9 and i < 9 and board[i][j] == '.':
                break
            i += 1
            j = 0
        if i == 9:
            return board
        board = self.check(board, i, j)[1]
        return board

    def check(self, board, i, j):
        right = 0
        i0 = i
        j0 = j
        for k in range(1, 10):
            i = i0
            j = j0
            if self.right(board, i, j, k):
                boardnow = board[::]
                boardnow[i] = boardnow[i][::]
                boardnow[i][j] = str(k)
                while i < 9:
                    while j < 9:
                        if boardnow[i][j] != '.':
                            j += 1
                        else:
                            break
                    if j < 9 and i < 9 and board[i][j] == '.':
                        break
                    i += 1
                    j = 0
                if i == 9:
                    return [1, boardnow]
                result = self.check(boardnow, i, j)
                if result[0]:
                    return result
        return [0, 0]

    def right(self, board, i, j, k):
        k = str(k)
        if k in board[i]:
            return False
        for m in range(9):
            if board[m][j] == k:
                return False
        x = i // 3
        y = j // 3
        for m in range(3):
            for n in range(3):
                if board[3 * x + m][3 * y + n] == k:
                    return False
        return True


A = Solution()

'''
trueboard = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
             ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
             ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
             ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
             ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
             ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
             ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
             ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
             ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
'''

board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

result = A.solveSudoku(board)
for i in range(9):
    for j in range(9):
        print(result[i][j], end=' ')
    print()

'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.v = {val for i in range(9) for j in range(9)
                    for val in [(i,board[i][j]), (board[i][j], j), (i//3, j//3, board[i][j])]}
    
        self.dfs(board, 0)
        
    def dfs(self, board, index):
        i = index // 9
        j = index % 9
        if i == 9:
            return True
        
        if board[i][j] != '.':
            return self.dfs(board, index + 1)
        else:
            for cand in '123456789':
                if {(i, cand), (cand,j), (i//3, j//3, cand)} & self.v:
                    continue
                else:
                    board[i][j]=cand
                    self.v |= {(i, cand), (cand,j), (i//3, j//3, cand)}
                    res = self.dfs(board, index + 1)
                    if res:
                        return True
                    else:
                        board[i][j]='.'
                        self.v -= {(i, cand), (cand,j), (i//3, j//3, cand)}
'''
