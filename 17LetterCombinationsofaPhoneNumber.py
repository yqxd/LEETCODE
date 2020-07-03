'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digits = str(digits)
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
             '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for i in digits:
            result1 = []
            for k in result:
                result1 += [k] * len(d[i])
            result = result1
            for j in range(len(result)):
                result[j] += d[i][j % len(d[i])]
        return result


A = Solution()
print(A.letterCombinations('23'))
