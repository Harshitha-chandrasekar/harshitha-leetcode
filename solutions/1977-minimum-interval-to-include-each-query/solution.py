class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
        
        ans = [-1] * len(queries)
        min_heap = []
        i = 0
        
        for q, original_index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                size = end - start + 1
                heapq.heappush(min_heap, (size, end))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                ans[original_index] = min_heap[0][0]
                
        return ans
