'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:(i + n)] == needle:
                return i
        return -1


A = Solution()
print(A.strStr('hello', 'll'))
