'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        if nums == []:
            return [[]]
        resulti = self.permuteUnique(nums[1:])
        for i in resulti:
            result += [[nums[0]] + i]
        now = 1
        while now < len(nums):
            if nums[now] != nums[now - 1]:
                resulti = self.permuteUnique(nums[0:now] + nums[now + 1:])
                for i in resulti:
                    result += [[nums[now]] + i]
            now += 1
        return result


A = Solution()
print(A.permuteUnique([1, 1, 2]))
