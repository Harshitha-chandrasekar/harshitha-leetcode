class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        totalsum = sum(stones)

        target = ceil(totalsum/2)
        def func(i,currsum):
            if currsum > target or i == len(stones):
                return abs(currsum - (totalsum - currsum))
            if (i,currsum) in dp:
                return dp[(i,currsum)]
            
            dp[(i,currsum)] = min(func(i+1,currsum),func(i+1,currsum+stones[i]))
            return dp[(i,currsum)]

        return func(0,0)
