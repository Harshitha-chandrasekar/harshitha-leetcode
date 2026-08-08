class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,ocean,prevh):
            if r not in range(rows) or c not in range(cols) or (r,c) in ocean or heights[r][c] < prevh:
                return

            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c,ocean,heights[r][c])
            dfs(r,c+1,ocean,heights[r][c])            
            dfs(r,c-1,ocean,heights[r][c])
            
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atlantic,heights[r][cols-1])

        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                pair = (r,c)
                if pair in atlantic and pair in pacific:
                    res.append([r,c])

        return res
