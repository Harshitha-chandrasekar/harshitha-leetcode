class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        if not occupiedIntervals:
            return []

        occupiedIntervals.sort(key=lambda x: x[0])

        merged = [occupiedIntervals[0]]

        for i in range(1,len(occupiedIntervals)):
            if occupiedIntervals[i][0]<=merged[-1][1]+1:
                merged[-1][1] = max(merged[-1][1],occupiedIntervals[i][1])
            else:
                merged.append(occupiedIntervals[i])

        res = []

        for start,end in merged:
            if start>freeEnd or end<freeStart:
                res.append([start,end])
            else:
                if start<freeStart:
                    res.append([start,freeStart-1])
                if end>freeEnd:
                    res.append([freeEnd+1,end])

        return res
