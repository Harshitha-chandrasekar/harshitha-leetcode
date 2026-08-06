class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        l = 0
        r = len(height) - 1
        while l<r:
            maxwater = max(maxwater,(r-l)*min(height[r],height[l]))
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1

        return maxwater
