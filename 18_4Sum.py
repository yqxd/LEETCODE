'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.
'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        s = []
        for i in d:
            for j in d:
                for k in d:
                    l = target - i - j - k
                    if i <= j and j <= k and k <= l and l in d:
                        if target % 4 == 0 and i == target // 4 and j == target // 4 and k == target // 4 and d[
                            target // 4] >= 4:
                            t = [1, [i, i, i, i]]
                        elif i == j and j < k and k < l and d[i] >= 2:
                            t = [1, [i, i, k, l]]
                        elif i < j and j == k and k < l and d[j] >= 2:
                            t = [1, [i, j, k, l]]
                        elif i < j and j < k and k == l and d[k] >= 2:
                            t = [1, [i, j, k, l]]
                        elif i == j and j == k and k < l and d[i] >= 3:
                            t = [1, [i, j, k, l]]
                        elif i < j and j == k and k == l and d[j] >= 3:
                            t = [1, [i, j, k, l]]
                        elif i == j and j < k and k == l and d[i] >= 2 and d[k] >= 2:
                            t = [1, [i, j, k, l]]
                        elif i < j and j < k and k < l:
                            t = [1, [i, j, k, l]]
                        else:
                            t = [0]
                    else:
                        t = [0]
                    if t[0]:
                        s += [t[1]]
        return s


A = Solution()
print(A.fourSum([1, 0, -1, 0, -2, 2], 0))
