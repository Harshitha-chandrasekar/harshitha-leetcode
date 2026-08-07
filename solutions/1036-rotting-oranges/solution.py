class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        time = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh +=1

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while fresh>0 and rotten:
            l = len(rotten)
            for i in range(l):
                r,c = rotten.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr,c+dc
                    if (nr>=0 and nr<rows and nc>=0 and nc<cols):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -=1
                            rotten.append((nr,nc))

            time +=1

        

        if fresh != 0:
            return -1
        return time
