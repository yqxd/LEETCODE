'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) - 1
        l = 0
        while n >= 0 and s[n] == ' ':
            n -= 1
        while n >= 0 and s[n] != ' ':
            l += 1
            n -= 1
        return l


A = Solution()
print(A.lengthOfLastWord("Hello World"))
