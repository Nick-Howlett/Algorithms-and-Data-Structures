#https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x: x[0])
        current = intervals[0]
        ret = []
        for interval in intervals[1:]:
            if interval[0] > current[1]:
                ret.append(current)
                current = interval
            else:
                current[1] = max(current[1], interval[1])
        ret.append(current)
        return ret