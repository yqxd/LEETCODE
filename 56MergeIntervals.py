'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        if len(intervals) <= 1:
            return intervals
        intervals.sort()
        now = 1
        while True:
            if now == len(intervals):
                return intervals
            else:
                if intervals[now][0] <= intervals[now - 1][1]:
                    intervals[now - 1][1] = max(intervals[now][1], intervals[now - 1][1])
                    del intervals[now]
                else:
                    now += 1


A = Solution()
print(A.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
