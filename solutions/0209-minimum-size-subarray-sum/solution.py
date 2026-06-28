class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        currsum = 0
        l = 0

        for r in range(len(nums)):
            currsum +=nums[r]
            while currsum>=target:
                min_l = min(min_l,r-l+1)
                currsum-=nums[l]
                l = l+1
            

        return 0 if min_l == float('inf') else min_l
