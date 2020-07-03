'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        else:
            result = [[]]
            for i in range(len(nums)):
                loc = self.subsets(nums[(i+1):])
                for j in loc:
                    result += [[nums[i]] + j]
            return result

A  = Solution()
print(A.subsets([1,2,3]))

