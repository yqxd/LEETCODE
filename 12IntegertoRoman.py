'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        k = ''
        r = num % 10
        num = num // 10
        if r == 4:
            k = 'IV' + k
        elif r == 9:
            k = 'IX' + k
        elif r >= 5:
            k = 'V' + 'I' * (r - 5) + k
        else:
            k = 'I' * r + k
        if num == 0:
            return k
        else:
            r = num % 10
            num = num // 10
            if r == 4:
                k = 'XL' + k
            elif r == 9:
                k = 'XC' + k
            elif r >= 5:
                k = 'L' + 'X' * (r - 5) + k
            else:
                k = 'X' * r + k
            if num == 0:
                return k
            else:
                r = num % 10
                num = num // 10
                if r == 4:
                    k = 'CD' + k
                elif r == 9:
                    k = 'CM' + k
                elif r >= 5:
                    k = 'D' + 'C' * (r - 5) + k
                else:
                    k = 'C' * r + k
                return num * 'M' + k


A = Solution()
print(A.intToRoman(3994))
