'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        p = self.check(0, intervals, newInterval)
        q = self.check(1, intervals, newInterval)
        if p - q == 0:
            if q == 0:



    def check(self, k, intervals, newInterval):
        p = 0
        q = len(intervals) - 1
        while True:
            if q - p == 0:
                return q
            elif q - p == 1:
                if intervals[p][k] >= newInterval[k]:
                    return p
                elif intervals[q][k] >= newInterval[k]:
                    return q
                else:
                    return q + 1
            else:
                middle = (p + q) // 2
                if intervals[middle][k] >= newInterval[k]:
                    q = middle
                else:
                    p = middle
'''

'''
# Simply add the new interval in the intervals list and repeat the operations of the Problem "MERGE INTERVALS"
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > stack[-1][1]:
                stack.append(intervals[i])
            else:
                stack[-1] = [stack[-1][0], max(stack[-1][1], intervals[i][1])]

        return stack
'''


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return [newInterval]
        if newInterval == []:
            return intervals
        now = 0
        while True:
            if newInterval[1] < intervals[now][0]:
                intervals.insert(now, newInterval)
                return intervals
            elif newInterval[1] <= intervals[now][1]:
                intervals[now][0] = min(intervals[now][0], newInterval[0])
                return intervals
            elif newInterval[0] > intervals[now][1]:
                now += 1
                if now == len(intervals):
                    intervals.append(newInterval)
                    return intervals
            else:
                newInterval[0] = min(intervals[now][0], newInterval[0])
                intervals.pop(now)
                if now == len(intervals):
                    intervals.append(newInterval)
                    return intervals


A = Solution()
a = [[1, 5]]
b = [6, 8]
print(A.insert(a, b))
