'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return 0
        step = [float('inf') for i in range(len(nums))]
        step[0] = 0
        now = 1
        for i in range(n):
            m = min(i + nums[i] + 1, n)
            for j in range(now, m):
                step[j] = min(step[j], step[i] + 1)
            now = m
        return step[-1]


A = Solution()
print(A.jump([2, 3, 1, 1, 4]))
