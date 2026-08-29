class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxarr = [float('-inf')]*n
        minarr = [float('inf')]*n
        globalmax = nums[0]
        maxarr[0] = nums[0]
        minarr[0] = nums[0]

        for i in range(1,n):
            currmax = max(maxarr[i-1]*nums[i],minarr[i-1]*nums[i],nums[i])
            currmin = min(maxarr[i-1]*nums[i],minarr[i-1]*nums[i],nums[i])

            maxarr[i] = max(currmax,currmin)
            minarr[i] = min(currmax,currmin)

            globalmax = max(currmax,globalmax)

        return globalmax
