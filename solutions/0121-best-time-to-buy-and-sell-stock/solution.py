class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxp = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                p = prices[r] - prices[l]
                maxp = max(maxp,p)
            else:
                l = r
            r = r+1

        return maxp
