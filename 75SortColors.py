'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return []
        i = 0
        j = 0
        k = 0
        for m in nums:
            if m == 0:
                i += 1
            elif m == 1:
                j += 1
            else:
                k += 1
        k = i + j + k - 1
        j = i + j - 1
        now = 0
        while True:
            if now == i:
                break
            elif nums[now] == 0:
                now += 1
            elif nums[now] == 1:
                nums[now], nums[j] = nums[j], nums[now]
                j -= 1
            else:
                nums[now], nums[k] = nums[k], nums[now]
                k -= 1
        if now > j:
            return nums
        while True:
            if now == j + 1:
                break
            elif nums[now] == 1:
                now += 1
            else:
                nums[now], nums[k] = nums[k], nums[now]
                k -= 1
        return nums


A = Solution()
print(A.sortColors([2, 1]))
