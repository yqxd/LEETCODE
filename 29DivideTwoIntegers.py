'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        k = dividend / divisor
        if k < -2147483648 or k > 2147483647:
            return 2147483647
        if k >= 0:
            return int(k)
        else:
            return -int(-dividend / divisor)


A = Solution()
print(A.divide(7, -3))
