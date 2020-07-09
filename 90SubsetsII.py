'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        keys = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                keys += [i]
        result = [[]]
        return self.subsetsone(result, d, keys)

    def subsetsone(self, result, d, keys):
        if keys == []:
            return result
        else:
            n = len(result)
            result = result * (d[keys[0]] + 1)
            for i in range(d[keys[0]] + 1):
                for j in range(n):
                    result[i * n + j] = result[i * n + j][::] + [keys[0]] * i
            return self.subsetsone(result, d, keys[1:])


A = Solution()
print(A.subsetsWithDup([1, 2, 2]))
