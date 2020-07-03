'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minnum = 0
        now = 0
        cha = -float('inf')
        for i in nums:
            now += i
            if now - minnum > cha:
                cha = now - minnum
            if now < minnum:
                minnum = now
        return cha


A = Solution()
print(A.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
