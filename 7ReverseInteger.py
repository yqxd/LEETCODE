'''
Given a 32-bit signed integer, reverse digits of an integer.
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        if x < 0:
            t = -1
            x = -x
        elif x == 0:
            return 0
        else:
            t = 1
        while not x % 10:
            x = x // 10
        k = 0
        while x:
            k = 10 * k
            k += x % 10
            x = x // 10
        k = t * k
        if k > math.pow(2, 31) - 1 or k < -math.pow(2, 31):
            return 0
        return k
