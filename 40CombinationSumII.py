'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidates.reverse()
        return self.check(candidates, target)

    def check(self, candidates, target):
        if target == 0:
            return [[]]
        if candidates == [] or candidates[-1] > target:
            return None
        now = candidates[0]
        num = 1
        while num < len(candidates) and candidates[num] == now:
            num += 1
        result = []
        for i in range(num + 1):
            add = self.check(candidates[num:], target - i * now)
            if add != None:
                for j in range(len(add)):
                    add[j] = [now] * i + add[j]
                result += add
        return result


A = Solution()
print(A.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
