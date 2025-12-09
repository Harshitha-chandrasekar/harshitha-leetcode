class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nummap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in nummap:
                return [i,nummap[comp]]

            nummap[num] = i
        
