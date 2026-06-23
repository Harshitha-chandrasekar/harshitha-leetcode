class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        bigg = 0
        for n in numset:
            if n-1 not in numset:
                x = n
                curr = 0
                while x in numset:
                    x = x+1
                    curr = curr+1
                bigg = max(bigg,curr)
        return bigg
