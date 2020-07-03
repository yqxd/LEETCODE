class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        return len(nums)


A = Solution()
print(A.removeDuplicates([1, 1, 2]))
print(A.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
