'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        k = k - 1
        A = [i for i in range(1, n + 1)]
        now = n - 1
        result = ''
        while now >= 0:
            loc = k // math.factorial(now)
            k = k % math.factorial(now)
            result += str(A[loc])
            A.pop(loc)
            now -= 1
        return result


A = Solution()
print(A.getPermutation(3, 3))
