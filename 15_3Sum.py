'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
'''


class Solution(object):
    def threeSum(self, nums):
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
                t = self.pubt(i, j, d, 0)
                if t[0]:
                    s += [t[1]]
        return s

    def pubt(self, i, j, A, c):
        k = c - i - j
        if i <= j and j <= k and k in A:
            if c % 3 == 0 and i == c // 3 and j == c // 3 and A[c // 3] >= 3:
                return [1, [0, 0, 0]]
            elif i == j and k > i and A[i] >= 2:
                return [1, [i, i, k]]
            elif i < j and j == k and A[j] >= 2:
                return [1, [i, j, j]]
            elif i < j and j < k:
                return [1, [i, j, k]]
            else:
                return [0]
        else:
            return [0]


A = Solution()
print(A.threeSum([1, 2, -2, -1]))
