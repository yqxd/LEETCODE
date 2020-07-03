'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

'''
also solution,but to slow.
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        d = [[[0, 0] for j in range(n)] for i in range(n)]
        for i in range(1, n + 1):
            if s[i - 1] == '(':
                d[i - 1][i - 1] = [0, 1]
            else:
                d[i - 1][i - 1] = [1, 0]
        maxlen = 0
        for j in range(1, n):
            for i in range(1, n - j + 1):
                d[i - 1][i + j - 1] = d[i - 1][i + j - 2][::]
                if s[i + j - 1] == ')':
                    if d[i - 1][i + j - 1][1] > 0:
                        d[i - 1][i + j - 1][1] -= 1
                        if d[i - 1][i + j - 1] == [0, 0]:
                            maxlen = j + 1
                    else:
                        d[i - 1][i + j - 1][0] += 1
                else:
                    d[i - 1][i + j - 1][1] += 1
        return maxlen
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        stack = []
        valid = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack += [i]
            else:
                if stack != []:
                    stack.pop(-1)
                    if stack == []:
                        if maxlen < i - valid + 1:
                            maxlen = i - valid + 1
                    else:
                        now = stack[-1] + 1
                        if maxlen < i - now + 1:
                            maxlen = i - now + 1
                else:
                    valid = i + 1
                    stack = []
        return maxlen


A = Solution()
print(A.longestValidParentheses("()(()"))
