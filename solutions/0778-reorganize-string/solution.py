class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        minHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(minHeap)
        prev = None
        ans = ""
        while prev or minHeap:
            if prev and not minHeap:
                return ""

            cnt, char = heapq.heappop(minHeap)
            cnt+=1
            ans+=char

            if prev:
                heapq.heappush(minHeap,prev)
                prev = None

            if cnt!=0:
                prev = [cnt,char]

        return ans
