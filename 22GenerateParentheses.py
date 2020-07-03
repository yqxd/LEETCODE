'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        result = ['']
        k = [0]
        for i in range(1, 2 * n + 1):
            for j in range(1, len(k) + 1):
                if k[j - 1] == 0:
                    k[j - 1] += 1
                    result[j - 1] += '('
                elif k[j - 1] == 2 * n - i + 1:
                    k[j - 1] -= 1
                    result[j - 1] += ')'
                else:
                    k += [k[j - 1] - 1]
                    result += [result[j - 1] + ')']
                    k[j - 1] += 1
                    result[j - 1] += '('
        return result


A = Solution()
print(A.generateParenthesis(0))
