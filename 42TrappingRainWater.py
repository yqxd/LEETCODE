'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        if height[0] > height[-1]:
            height.reverse()
        index = 1
        num = 0
        while index < len(height):
            if height[index] >= height[0]:
                return num + self.trap(height[index:])
            else:
                num += height[0] - height[index]
                index += 1


A = Solution()
print(A.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
