class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cache = [-1]*n

        def df(val):
            if val>=n:
                return 0
            if cache[val]!=-1:
                return cache[val]

            rob = nums[val] + df(val+2)
            skip = df(val+1)
            cache[val] = max(rob,skip)

            return cache[val]

        return df(0)
