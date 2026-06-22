class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in hashmap:
                return [i,hashmap[diff]]
            else:
                hashmap[n]=i
