class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or (i,j) in visited or board[i][j] == 'X':
                return

            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return


        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[rows-1][c] == 'O':
                dfs(rows-1,c)

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
