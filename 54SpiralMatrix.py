'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix[0] == []:
            return []
        if len(matrix) > len(matrix[0]):
            l = 2 * len(matrix[0])
        else:
            l = 2 * len(matrix) - 1
        result = []
        for i in range(1, l + 1):
            result += self.del_matrix(matrix, i % 4)
        return result

    def del_matrix(self, matrix, i):
        if i == 1:
            return matrix.pop(0)
        elif i == 3:
            m = matrix.pop(-1)
            m.reverse()
            return m
        elif i == 2:
            result = []
            for i in range(len(matrix)):
                result += [matrix[i].pop(-1)]
            return result
        else:
            result = []
            for i in range(len(matrix) - 1, -1, -1):
                result += [matrix[i].pop(0)]
            return result


A = Solution()
matrix = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
print(A.spiralOrder(matrix))
print(matrix)
