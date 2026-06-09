class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        minimum = [('inf')]*n
        maximum = [('-inf')]*n
        global_max = nums[0]
        maximum[0] = nums[0]
        minimum[0] = nums[0]

        for i in range(1,n):
            curr_max = max(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])
            curr_min = min(maximum[i-1]*nums[i],minimum[i-1]*nums[i],nums[i])

            maximum[i] = max(curr_max,curr_min)
            minimum[i] = min(curr_max,curr_min)

            global_max = max(global_max,maximum[i],minimum[i])

        return global_max
