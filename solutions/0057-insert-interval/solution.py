class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        i = 0
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i = i+1

        while i<len(intervals) and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i = i+1
        ans.append(newInterval)

        while i<len(intervals):
            ans.append(intervals[i])
            i = i+1

        return ans
