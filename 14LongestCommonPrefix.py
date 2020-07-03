'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        l = len(strs[0])
        for i in range(0, len(strs) - 1):
            k = 0
            l = min(l, len(strs[i]) - 1, len(strs[i + 1]) - 1)
            while k <= l:
                if strs[i][k] != strs[i + 1][k]:
                    l = k - 1
                    break
                else:
                    k = k + 1
        return strs[0][:(l + 1)]


A = Solution()
print(A.longestCommonPrefix(["aa", 'a']))
