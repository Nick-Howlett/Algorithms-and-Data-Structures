class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        for interval in intervals:
            if self.overlaps(interval, newInterval):
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                ret.append(interval)
        ret.append(newInterval)
        return sorted(ret, key = lambda x: x[0])
    
    
    
    def overlaps(self, interval1, interval2):
        return ((interval2[0] >= interval1[0] and interval2[1] <= interval1[1]) or
            (interval1[0] >= interval2[0] and interval1[1] <= interval2[1]) or
           (interval2[0] > interval1[0] and interval2[0] <= interval1[1]) or
           (interval2[1] < interval1[1] and interval2[1] >= interval1[0]))