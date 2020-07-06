'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n <= 3:
            for i in range(n):
                if nums[i] == target:
                    return True
            return False
        elif nums[0] < nums[n - 1]:
            mid = n // 2
            if nums[mid] == target or nums[0] == target or nums[n - 1] == target:
                return True
            elif nums[mid] > target:
                return self.search(nums[0:mid], target)
            elif nums[mid] < target:
                return self.search(nums[mid:n], target)
            else:
                return self.search(muns[0:mid] + nums[(mid + 1):n], target)
        elif nums[0] > nums[n - 1]:
            mid = n // 2
            if nums[mid] == target or nums[0] == target or nums[n - 1] == target:
                return True
            elif nums[mid] > nums[0]:
                if target > nums[mid] or target < nums[n - 1]:
                    return self.search(nums[mid:n], target)
                else:
                    return self.search(nums[0:mid], target)
            elif nums[mid] < nums[0]:
                if target > nums[0] or target < nums[mid]:
                    return self.search(nums[0:mid], target)
                else:
                    return self.search(nums[mid:n], target)
            else:
                return self.search(nums[0:mid] + nums[(mid + 1):n], target)
        else:
            return self.search(nums[1:n], target)


A = Solution()
print(A.search([2, 2, 2, 0, 1], 0))
