class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        sum = 0
        for i in range(k):
            x = nums[i]
            if mul>1:
                sum = sum + (x*mul)
            else:
                sum = sum+x
            mul = mul-1
        return sum
