'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
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
                    t = self.pubt_closest(i, j, k, d)
                    if t:
                        if i + j + k == target:
                            return target
                        s += [i + j + k]
        if len(s) == 0:
            return None
        t = s[0]
        for i in range(len(s)):
            if abs(target - t) > abs(s[i] - target):
                t = s[i]
        return t

    def pubt_closest(self, i, j, k, A):
        if i <= j and j <= k:
            if i == j and j == k and A[i] >= 3:
                return 1
            elif i == j and k > i and A[i] >= 2:
                return 1
            elif i < j and j == k and A[j] >= 2:
                return 1
            elif i < j and j < k:
                return 1
            else:
                return 0
        else:
            return 0


A = Solution()
print(A.threeSumClosest(
    [-63, -15, -88, 58, 4, 67, -95, -39, 11, -42, -100, 56, 53, 43, -80, 78, 0, 74, 100, -79, -34, -84, 3, 47, -44, 45,
     -45, 26, -47, 14, 48, 68, -52, -3, -5, 88, -60, 35, 26, 43, -37, 46, 88, -12, -74, -60, -85, 37, 0, 20, -54, 12,
     -10, 76, 28, -39, 5, 80, 89, 26, 84, -85, 79, 37, -94, -51, -63, -61, -76, -76, -21, 1, -31, -18, -38, -83, 96,
     -23, 87, -85, 16, -26, -65, -18, -90, -44, -41, 69, -59, -59, 97, 51, -6, -31, -33, 72, -18, -27, 51, 22, -6, 49,
     -44, -52, 71, -65, 17, 92, -89, 15, -71, 36, 17, 4, 42, -40, 25, 27, 72, -37, -90, -42, -50, -97, 21, 26, -31, -47,
     -59, -82, 77, -14, 76, 70, 87, -22, -74, 16, -29, -96, 57, -9, -16, -2, 6, -41, -72, -84, -29, 28, 25, -24, 13, 21,
     52, -59, 71, 29, 23, -28, 83, 11, -57, 0, -13, 33, -11, 35, -30, 99, -39, -57, -58, 63, 84, 76], 48
))
