'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        now1 = 0
        now2 = m
        nums1[m:(m + n)] = nums2
        while True:
            if now2 == m + n or now1 == now2:
                return nums1
            elif nums1[now1] <= nums1[now2]:
                now1 += 1
            else:
                nums1[now1:(now2 + 1)] = [nums1[now2]] + nums1[now1:now2]
                now2 += 1
                now1 += 1


A = Solution()
print(A.merge([4, 0, 0, 0, 0, 0],
              1,
              [1, 2, 3, 5, 6],
              5))
