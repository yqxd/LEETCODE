'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ''
        d = [[-1 for i in range(n)] for i in range(n)]
        for i in range(0, n + 1, 1):
            d[i - 1][i - 1] = 1
        for i in range(0, n, 1):
            d[i][i - 1] = 0
        maxlen = 1
        maxstr = s[0]
        for i in range(1, n + 1, 1):
            for j in range(1, n - i + 1, 1):
                if d[j][j + i - 2] == -1 or s[j - 1] != s[i + j - 1]:
                    d[j - 1][i + j - 1] = -1
                else:
                    d[j - 1][i + j - 1] = d[j][i + j - 2] + 2
                    if i + 1 > maxlen:
                        maxlen = i + 1
                        maxstr = s[j - 1:i + j]
        return maxstr
