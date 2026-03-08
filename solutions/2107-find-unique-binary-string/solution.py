class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums[0])
        intnums = []
        for i in nums:
            intnums.append(int(i,2))
        x = 0
        while True:
            if x not in intnums:
                return bin(x)[2:].zfill(n)
            x = x + 1

    
