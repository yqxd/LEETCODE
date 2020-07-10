'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        elif len(s) == 0:
            return 1
        d = {0: 1, 1: 1}
        now = 2
        while True:
            if now == len(s) + 1:
                return d[len(s)]
            else:
                if (s[now - 1] in ['1', '2', '3', '4', '5', '6'] and s[now - 2] == '2') or s[now - 2] == '1':
                    if (len(s) >= now + 1 and s[now] == '0') or s[now - 1] == '0':
                        d[now] = d[now - 1]
                    else:
                        d[now] = d[now - 2] + d[now - 1]
                elif s[now - 1] == '0':
                    if s[now - 2] == '1' or s[now - 2] == '2':
                        d[now] = d[now - 1]
                    else:
                        return 0
                else:
                    d[now] = d[now - 1]
                now += 1


A = Solution()
print(A.numDecodings('17'))
