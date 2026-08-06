class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def check(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
                return

            grid[i][j] = '.'
            check(i+1,j)
            check(i-1,j)
            check(i,j+1)
            check(i,j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    check(i,j)
                    count+=1

        return count
