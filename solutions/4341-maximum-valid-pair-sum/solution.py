class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k>=n:
            return 0
        suffix = [float('-inf')]*n
        curr = float('-inf')

        for i in range(n-1,-1,-1):
            curr = max(curr,nums[i])
            suffix[i] = curr

        ans = float('-inf')
        for i in range(n-k):
            if i+k<n:
                ans = max(ans,nums[i]+suffix[i+k])

        return ans
