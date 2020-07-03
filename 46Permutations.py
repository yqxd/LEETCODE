'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        result = []
        for i in range(len(nums)):
            resulti = self.permute(nums[0:i] + nums[i + 1:])
            for j in resulti:
                result += [[nums[i]] + j]
        return result


A = Solution()
print(A.permute([1, 2, 3]))
