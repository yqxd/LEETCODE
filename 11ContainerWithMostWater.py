'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        head = 0
        tail = len(height) - 1
        water = min(height[tail], height[head]) * (tail - head)
        while tail > head:
            if height[tail] > height[head]:
                head += 1
            else:
                tail -= 1
            k = min(height[tail], height[head]) * (tail - head)
            if k > water:
                water = k
        return water


A = Solution()
print(A.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
