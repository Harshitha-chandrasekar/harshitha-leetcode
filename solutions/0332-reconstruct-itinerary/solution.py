class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        adj = defaultdict(list)
        for src,des in sorted(tickets)[::-1]:
            adj[src].append(des)

        heap = []
        def dfs(src):
            while adj[src]:
                des = adj[src].pop()
                dfs(des)
            heap.append(src)

        dfs('JFK')
        return heap[::-1]
