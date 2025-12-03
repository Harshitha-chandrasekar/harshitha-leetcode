class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0
        i =0
        while i< len(nums):
            
            right_sum = right_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum = left_sum + nums[i]

            i = i+1

        return -1
