'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.resone(s, 4)

    def resone(self, s, n):
        if n == 1:
            if s == '' or (len(s) >= 2 and s[0] == '0') or eval(s) > 255:
                return []
            else:
                return [s]
        else:
            result = []
            for i in self.resone(s[1:], n - 1):
                result += [s[0] + '.' + i]
            if len(s) >= 3 and s[0] != '0':
                for i in self.resone(s[2:], n - 1):
                    result += [s[0:2] + '.' + i]
            if len(s) >= 4 and s[0] != '0' and eval(s[0:3]) <= 255:
                for i in self.resone(s[3:], n - 1):
                    result += [s[0:3] + '.' + i]
            return result


A = Solution()
print(A.resone("010010", 4))
