'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if nums[-1 - i] < nums[-1]:
                k = 1
                while nums[-1 - i] < nums[-k] and k < 1 + i:
                    k += 1
                nums[- 1 - i], nums[-k + 1] = nums[-k + 1], nums[- 1 - i]
                return nums
            else:
                k = nums[-1 - i]
                del nums[-1 - i]
                nums += [k]
        nums.reverse()
        return nums


A = Solution()
print(A.nextPermutation([1, 3, 2]))
