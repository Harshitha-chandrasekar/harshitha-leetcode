class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = [amount+1] * (amount+1)
        cache[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    cache[a] = min(cache[a],1+cache[a-c])

        if cache[amount] != amount+1:
            return cache[amount]
        else:
            return -1
        
