class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        
        curr_max = nums[0]
        total_max = nums[0]
        
        for i in range(1, len(nums)):
            current_num = nums[i]
        
            curr_max = max(current_num, curr_max + current_num)

            total_max = max(total_max, curr_max)
            
        return total_max
