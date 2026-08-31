class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            arr[i][0] = 1
        for i in range(n):
            arr[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                arr[i][j] = arr[i][j-1] + arr[i-1][j]

        return arr[m-1][n-1]
