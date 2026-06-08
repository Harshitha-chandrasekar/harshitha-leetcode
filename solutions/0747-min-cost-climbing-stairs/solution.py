class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cache = [-1] * n

        def dp(val):
            if val>=n:
                return 0
            if cache[val]!=-1:
                return cache[val]

            cache[val] = cost[val] + min(dp(val+1),dp(val+2))
            return cache[val]

        return min(dp(0),dp(1))
