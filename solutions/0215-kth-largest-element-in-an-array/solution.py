class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-1*n for n in nums]
        heapq.heapify(neg)
        while k-1>0:
            k -=1
            heapq.heappop(neg)

        return -1*heapq.heappop(neg)
