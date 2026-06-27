class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1
        while l<r:
            water = (r-l)*min(height[l],height[r])
            ans = max(ans,water)
            if height[l]<height[r]:
                l = l+1
            else:
                r = r-1
        return ans
