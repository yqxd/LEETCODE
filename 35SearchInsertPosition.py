'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(tail) == 0:
            return 0
        head = 0
        tail = len(nums) - 1
        if nums[0] > target:
            return 0
        elif nums[tail] < target:
            return tail + 1
        while True:
            if tail - head == 1:
                return tail
            else:
                mid = (head + tail) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    head = mid
                else:
                    tail = mid


A = Solution()
print(A.searchInsert([1, 3, 5, 6], 7))
