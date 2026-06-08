class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        curr_sum = sum(nums)
        deficit = abs(goal - curr_sum)
        count = 0
        
        return (deficit+limit-1)//limit
