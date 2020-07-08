'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxlen = 0
        if matrix == []:
            return maxlen
        else:
            heights = [0 for i in range(len(matrix[0]))]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] == '1':
                        heights[j] += 1
                    else:
                        heights[j] = 0
                maxlen = max(maxlen, self.maximalRectangleOne(heights))
            return maxlen

    def maximalRectangleOne(self, heights):
        maxArea = 0
        stack = []  # stack of pairs: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        # remaining heights extended to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


A = Solution()
matrix = [
    ['0', '1'],
    ['1', '0']
]
print(A.maximalRectangle(matrix))
