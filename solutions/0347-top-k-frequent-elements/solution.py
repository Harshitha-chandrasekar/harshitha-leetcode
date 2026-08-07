class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqh = {}
        for n in nums:
            if n in freqh:
                freqh[n]+=1
            else:
                freqh[n]=1

        heap = []
        for key,count in freqh.items():
            heapq.heappush(heap,(-count,key))

        res = []
        while k>0:
            count,key = heapq.heappop(heap)
            res.append(key)
            k-=1
        return res
