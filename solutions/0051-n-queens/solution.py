class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def placeQ(i,cols,rightdiag,leftdiag,cur,res):
            n = len(cols)
            if i == n:
                res.append(["".join(row) for row in cur])
                return

            for j in range(n):
                if cols[j] or rightdiag[i+j] or leftdiag[i-j+n-1]:
                    continue

                cols[j] = 1
                rightdiag[i+j] = 1
                leftdiag[i-j+n-1] = 1
                cur[i][j] = 'Q'
                placeQ(i+1,cols,rightdiag,leftdiag,cur,res)
                cols[j] = 0
                rightdiag[i+j] = 0
                leftdiag[i-j+n-1] = 0
                cur[i][j] = '.'

        cols = [0]*n
        leftd = [0]*(n*2)
        rightd = [0]*(n*2)
        cur = [['.']*n for _ in range(n)]            
        res = []
        placeQ(0,cols,rightd,leftd,cur,res)
        return res

