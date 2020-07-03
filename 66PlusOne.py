'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k = 1
        now = len(digits) - 1
        while k == 1:
            if digits[now] == 9:
                digits[now] = 0
                now -= 1
                if now < 0:
                    break
            else:
                digits[now] += 1
                k = 0
        if k == 1:
            return [1] + digits
        return digits


A = Solution()
print(A.plusOne([9, 9, 9, 9]))
