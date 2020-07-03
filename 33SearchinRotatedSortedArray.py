'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        head = 0
        tail = len(nums) - 1
        if nums[head] == target:
            return head
        elif nums[tail] == target:
            return tail
        if len(nums) <= 2:
            return -1
        while True:
            if tail - head == 1:
                return -1
            else:
                mid = (head + tail) // 2
                if nums[head] < nums[tail]:
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] < target:
                        head = mid
                    else:
                        tail = mid
                else:
                    if nums[mid] == target:
                        return mid
                    if nums[mid] > nums[head]:
                        if target > nums[head] and target < nums[mid]:
                            tail = mid
                        else:
                            head = mid
                    else:
                        if target > nums[mid] and target < nums[tail]:
                            head = mid
                        else:
                            tail = mid


A = Solution()
print(A.search([4, 5, 6, 7, 0, 1, 2], 3))
