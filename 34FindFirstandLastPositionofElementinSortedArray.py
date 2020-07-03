'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        head = 0
        tail = len(nums) - 1
        if len(nums) <= 2:
            if nums[head] == target:
                if nums[tail] == target:
                    return [head, tail]
                else:
                    return [head, head]
            elif nums[tail] == target:
                return [tail, tail]
            else:
                return [-1, -1]
        if nums[head] == target:
            return [head, self.findone(nums, head, 1, target)]
        elif nums[tail] == target:
            return [self.findone(nums, tail, -1, target), tail]
        while True:
            if tail - head == 1:
                return [-1, -1]
            mid = (head + tail) // 2
            if nums[mid] == target:
                return [self.findone(nums, mid, -1, target), self.findone(nums, mid, 1, target)]
            elif nums[mid] > target:
                tail = mid
            else:
                head = mid

    def findone(self, nums, now, wh, target):
        if wh == -1:
            head = 0
            tail = now
            if head == tail:
                return head
            while True:
                if tail - head == 1:
                    if nums[head] == target:
                        return head
                    else:
                        return tail
                mid = (tail + head) // 2
                if nums[mid] == target:
                    tail = mid
                else:
                    head = mid
        else:
            head = now
            tail = len(nums) - 1
            if head == tail:
                return head
            while True:
                if tail - head == 1:
                    if nums[tail] == target:
                        return tail
                    else:
                        return head
                mid = (tail + head) // 2
                if nums[mid] == target:
                    head = mid
                else:
                    tail = mid


A = Solution()
print(A.searchRange([5, 7, 7, 8, 8, 10], 6))
