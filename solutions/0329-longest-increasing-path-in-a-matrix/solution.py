class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp ={}
        rows = len(matrix)
        cols = len(matrix[0])


        def dfs(i,j,prev):
            if i<0 or j<0 or i>=rows or j>=cols or matrix[i][j]<=prev:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            curr = matrix[i][j]
            res = 1
            res = max(res,1+dfs(i+1,j,curr))
            res = max(res,1+dfs(i-1,j,curr))
            res = max(res,1+dfs(i,j-1,curr))
            res = max(res,1+dfs(i,j+1,curr))

            dp[(i,j)] = res
            return res
        
        for i in range(rows):
            for j in range(cols):
                dp[(i,j)] = dfs(i,j,-1)

        return max(dp.values())
