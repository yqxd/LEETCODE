'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:

Input: [2,1,5,6,2,3]
Output: 10
'''


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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
print(A.largestRectangleArea([2, 1, 2]))
