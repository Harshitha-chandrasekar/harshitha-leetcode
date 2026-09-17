class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u,v,t in times:
            edges[u].append((v,t))

        heap = [[0,k]]
        visited = set()
        t = 0
        while heap:
            time,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,time)
            for nextnode, nexttime in edges[node]:
                if nextnode not in visited:
                    heapq.heappush(heap,[time+nexttime,nextnode])

        return t if len(visited) == n else -1
