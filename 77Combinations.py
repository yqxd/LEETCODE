'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.oneCombine([i for i in range(1, (n + 1))], k)

    def oneCombine(self, lists, k):
        if len(lists) == k:
            return [lists]
        elif k == 0:
            return [[]]
        else:
            result = []
            for i in range(0, len(lists) - k + 1):
                loc = self.oneCombine(lists[(i + 1):len(lists)], k - 1)
                for j in loc:
                    result += [[lists[i]] + j]
            return result


A = Solution()
print(A.oneCombine([1, 2, 3], 2))
