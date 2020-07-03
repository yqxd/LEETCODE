'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}': '{', ']': '[', ')': '('}
        stack = []
        index = -1
        if len(s) == 0:
            return True
        for i in s:
            if i in d:
                if index == -1 or stack[index] != d[i]:
                    return False
                else:
                    index -= 1
                    del stack[index + 1]
            else:
                stack += [i]
                index += 1
        if index == -1:
            return True


A = Solution()
print(A.isValid(']'))
