class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]
        ans = []
        for i in range(n):
            if i ==0:
                ans.append(suffix[1])
            elif i == n-1:
                ans.append(prefix[-2])
            else:
                ans.append(prefix[i-1]*suffix[i+1])
        return ans
