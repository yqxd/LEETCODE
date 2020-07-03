'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for i in strs:
            w = 0
            for j in range(len(result)):
                if self.check(result[j][0], i):
                    result[j] += [i]
                    w = 1
                    break
            if w == 0:
                result += [[i]]
        return result
    def check(self, a, b):
        a = list(a)
        b = list(b)
        a.sort()
        b.sort()
        if a == b:
            return True
        else:
            return False
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        d = {}
        num = 0
        for i in strs:
            w = 0
            now = list(i)
            now.sort()
            now = ''.join(now)
            if now in d:
                result[d[now]] += [i]
            else:
                result += [[i]]
                d[now] = num
                num += 1
        return result


A = Solution()
print(A.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
