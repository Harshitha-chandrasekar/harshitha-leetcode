class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = {0:1}
        count = 0
        curr_sum = 0
        for i in nums:
            curr_sum = curr_sum + i
            req = curr_sum - k
            count = count + prefix_sum.get(req,0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0) + 1
            
        return count

        
