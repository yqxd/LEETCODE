'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return [[]]
        if candidates == [] or min(candidates) > target:
            return None
        num = candidates[0]
        now = candidates[1:]
        result = []
        for i in range(target // num + 1):
            add = self.combinationSum(now, target - i * num)
            if add != None:
                for j in range(len(add)):
                    add[j] = [num] * i + add[j]
                result += add
        return result


A = Solution()
print(A.combinationSum([2, 3, 5], 8))
