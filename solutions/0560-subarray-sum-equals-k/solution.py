class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        curr = 0
        res = 0
        for n in nums:
            curr = curr+n
            if curr-k in prefix:
                res = res + prefix[curr-k]

            if curr in prefix:
                prefix[curr] = prefix[curr]+1
            else:
                prefix[curr] = 1
        return res
