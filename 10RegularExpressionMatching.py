'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        d = [[False for i in range(m+1)] for j in range(n+1)]
        w = 2
        while True:
            if w <= m and p[w-1] == '*':
                d[0][w] = True
                w = w + 2
            else:
                break
        d[0][0] = True
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '*':
                    if p[j-2] == '.':
                        w = False
                        for k in range(i, -1, -1):
                            if d[k][j-2]:
                                w = True
                                break
                        d[i][j] = w
                    else:
                        w = False
                        if d[i][j-2]:
                            w = True
                        else:
                            for k in range(i, 0, -1):
                                if s[k-1] == p[j-2]:
                                    if d[k-1][j-2]:
                                        w = True
                                        break
                                else:
                                    break
                        d[i][j] = w
                elif p[j-1] == '.':
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = d[i-1][j-1] and s[i-1] == p[j-1]
        return d[n][m]
A = Solution()
s = 'aab'
p = 'c*a*b'
print(A.isMatch(s, p))