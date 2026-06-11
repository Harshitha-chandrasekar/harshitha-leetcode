class Solution(object):
    def maximumTotalDamage(self, power):
        """
        :type power: List[int]
        :rtype: int
        """
        freq = Counter(power)

        nums = sorted(freq)
        gain = [x * freq[x] for x in nums]

        n = len(nums)
        dp = [0] * n

        for i in range(n):
            take = gain[i]

            # Find rightmost power < nums[i] - 2
            j = bisect_left(nums, nums[i] - 2) - 1

            if j >= 0:
                take += dp[j]

            skip = dp[i - 1] if i > 0 else 0

            dp[i] = max(take, skip)

        return dp[-1]
