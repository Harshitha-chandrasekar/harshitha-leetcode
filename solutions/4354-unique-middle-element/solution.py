from collections import Counter
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid_ele = nums[len(nums)//2]
        x = Counter(nums)
        if x[mid_ele] == 1:
            return True
        else:
            return False
