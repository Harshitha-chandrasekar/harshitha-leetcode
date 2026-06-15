class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')]*n
        dp[-1] = 0
        for i in range(n-2,-1,-1):
            curr_jump_ability = nums[i]
            for j in range(curr_jump_ability,-1,-1):
                if i+j<n:
                    dp[i] = min(dp[i],dp[i+j]+1)

        return dp[0]
