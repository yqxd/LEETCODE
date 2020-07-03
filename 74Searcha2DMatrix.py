'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        for i in range(1, m):
            matrix[0] += matrix[i]
        matrix = matrix[0]
        return self.bsearch(matrix, target)

    def bsearch(self, matrix, target):
        n = len(matrix)
        if n == 1:
            if matrix[0] == target:
                return True
            else:
                return False
        elif n == 0:
            return False
        else:
            n1 = n // 2
            if matrix[n1] < target:
                matrix = matrix[(n1+1):n]
                return self.bsearch(matrix, target)
            elif matrix[n1] > target:
                matrix = matrix[0:n1]
                return self.bsearch(matrix, target)
            else:
                return True

A = Solution()
print(A.searchMatrix([[1,2,3,4,5,6]], 2))