'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s == '' or t == '':
            return ''
        d = {}
        o = {}
        for i in t:
            if i not in d:
                d[i] = 0
                o[i] = 1
            else:
                o[i] += 1
        nownum = 0
        m = len(t)
        left = 0
        right = 0
        minnum = float('Inf')
        minstr = ""
        while True:
            if right == len(s) + 1:
                return minstr
            elif nownum == m:
                if minnum > right - left:
                    minnum = right - left
                    minstr = s[left:right]
                if s[left] in d:
                    d[s[left]] -= 1
                    if d[s[left]] < o[s[left]]:
                        nownum -= 1
                left += 1
            else:
                right += 1
                if right == len(s) + 1:
                    return minstr
                if s[right - 1] in d:
                    d[s[right - 1]] += 1
                    if d[s[right - 1]] <= o[s[right - 1]]:
                        nownum += 1


A = Solution()
S = "aa"
T = "a"
print(A.minWindow(S, T))
