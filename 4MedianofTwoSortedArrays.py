'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        while True:
            if len(nums2) == 1:
                if len(nums1) % 2 == 1:
                    if len(nums1) == 1:
                        return (nums1[0] + nums2[0]) / 2
                    if nums1[len(nums1) // 2] >= nums2[0]:
                        if nums1[len(nums1) // 2 - 1] <= nums2[0]:
                            return (nums1[len(nums1) // 2] + nums2[0]) / 2
                        else:
                            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
                    else:
                        if nums1[len(nums1) // 2 + 1] > nums2[0]:
                            return (nums1[len(nums1) // 2] + nums2[0]) / 2
                        else:
                            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 + 1]) / 2
                else:
                    if nums1[len(nums1) // 2] < nums2[0]:
                        return nums1[len(nums1) // 2]
                    elif nums1[len(nums1) // 2 - 1] > nums2[0]:
                        return nums1[len(nums1) // 2 - 1]
                    else:
                        return nums2[0]
            n1 = (len(nums1) - 1) // 2
            n2 = len(nums2) // 2
            if nums1[n1] > nums2[n2]:
                nums1 = nums1[:(len(nums1) - n2)]
                nums2 = nums2[n2:]
            else:
                nums1 = nums1[(len(nums2) - n2 - 1):]
                nums2 = nums2[:n2]
            if len(nums2) <= 2:
                for i in nums2:
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        return self.findKth(nums1, nums2, l // 2) if l % 2 == 1 else (self.findKth(nums1, nums2,
                                                                                   l // 2 - 1) + self.findKth(nums1,
                                                                                                              nums2,
                                                                                                              l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        assert k <= len(A) + len(B) - 1
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)
