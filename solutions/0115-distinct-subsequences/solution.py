class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        if len(t) > len(s):
            return 0

        def func(i,j):
            if j == len(t):
                return 1
                
            if i == len(s):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]

            res = func(i+1,j)
            if s[i] == t[j]:
                res += func(i+1,j+1)
            dp[(i,j)] = res
            return res

        return func(0,0)
