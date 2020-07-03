'''
Given a string, find the length of the longest substring without repeating characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        if len(s) == 0:
            return 0
        d[s[0]] = 0
        maxlen = 1
        nowlen = 1
        for i in range(1, len(s)):
            if s[i] not in d.keys():
                nowlen += 1
            else:
                if i-d[s[i]] > nowlen:
                    nowlen = nowlen + 1
                else:
                    if maxlen < nowlen:
                        maxlen = nowlen
                    nowlen = i - d[s[i]]
            d[s[i]] = i
        if nowlen > maxlen:
            return nowlen
        return maxlen