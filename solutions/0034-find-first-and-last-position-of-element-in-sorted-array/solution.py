class Solution(object):
    def searchRange(self, nums, target):
        first = -1
        last = -1
        for i in range(0,len(nums)):
            if(nums[i] == target):
                last = i
                if(first == -1):
                    first = i

        return first, last
        
