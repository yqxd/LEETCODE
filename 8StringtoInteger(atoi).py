'''
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
'''


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        t = ''
        k = 0
        while k < len(str):
            if str[k] == ' ':
                k += 1
            else:
                break
        if k < len(str) and str[k] in ['+', '-']:
            t += str[k]
            k += 1
        while k < len(str):
            if str[k] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                t += str[k]
                k += 1
            else:
                break
        if len(t) == 0 or t == '+' or t == '-':
            return 0
        k = int(t)
        if k < -2147483648:
            return -2147483648
        elif k > 2147483647:
            return 2147483647
        else:
            return k


A = Solution()
print(A.myAtoi("words and 987"))
print(A.myAtoi("-91283472332"))
print(A.myAtoi("4193 with words"))
print(A.myAtoi("   -42"))