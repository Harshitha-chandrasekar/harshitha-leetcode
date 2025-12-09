class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minimum = prices[0]

        max_profit = 0

        for i in range(1,len(prices)):
            p = prices[i] - minimum

            max_profit = max(max_profit, p)

            minimum = min(minimum, prices[i])

        return max_profit
