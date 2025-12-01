class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        leng = float('inf')

        n = len(nums)
        left = 0
        sum = 0
        for right in range(n):
            sum = sum + nums[right]
            while sum >= target:
                leng = min(leng, right - left + 1)
                sum = sum - nums[left]
                left = left + 1

        if leng == float('inf'):
            return 0
        return leng 
        
